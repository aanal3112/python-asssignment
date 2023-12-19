from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Coupon, RepeatCount
from .serializers import RepeatCountSerializer
from django.shortcuts import get_object_or_404
from datetime import timedelta
from django.utils import timezone
from django.contrib.auth.models import *
import requests


class AddRepeatCountsView(APIView):
    def post(self, request):
        try:
            coupon_code = request.data.get('coupon_code')
            if not coupon_code:
                return Response({"message": "Coupon code is required"}, status=status.HTTP_400_BAD_REQUEST)
            
            coupon, created = Coupon.objects.get_or_create(code=coupon_code)
        
            if 'per_user_total_repeat' in request.data:
                coupon.per_user_total_repeat = request.data.get('per_user_total_repeat')
            if 'per_user_daily_repeat' in request.data:
                coupon.per_user_daily_repeat = request.data.get('per_user_daily_repeat')
            if 'per_user_weekly_repeat' in request.data:
                coupon.per_user_weekly_repeat = request.data.get('per_user_weekly_repeat')
            if 'global_total_repeat' in request.data:
                coupon.global_total_repeat = request.data.get('global_total_repeat')
            coupon.save()
            return Response({'message':'coupon is created and repeat counts are added'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': str(e)},status=status.HTTP_400_BAD_REQUEST)

from django.utils import timezone
from datetime import timedelta

class VerifyCouponValidity(APIView):
    def post(self, request):
        try:
            coupon_code = request.data.get('coupon_code')
            
            if not coupon_code:
                return Response({"message": "Coupon code is required"}, status=status.HTTP_400_BAD_REQUEST)
            
            coupon = Coupon.objects.get(code=coupon_code)
            global_total_repeat = RepeatCount.objects.filter(coupon=coupon).count()
            user_daily_repeat = RepeatCount.objects.filter(coupon=coupon, created_at__gte=timezone.now() - timedelta(days=1)).count()
            user_weekly_repeat = RepeatCount.objects.filter(coupon=coupon, created_at__gte=timezone.now() - timedelta(weeks=1)).count()
            user_total_repeat = RepeatCount.objects.filter(coupon=coupon).count()

            if coupon.global_total_repeat <= global_total_repeat:
                return Response({'message': "Global total repeat for this coupon has been exceeded"}, status=status.HTTP_400_BAD_REQUEST)
            
            if coupon.per_user_total_repeat <= user_total_repeat:
                return Response({'message': "Total repeat limit for this coupon for a user has been exceeded"}, status=status.HTTP_400_BAD_REQUEST)

            if coupon.per_user_weekly_repeat <= user_weekly_repeat:
                return Response({'message': "Weekly repeat limit for this coupon for a user has been exceeded"}, status=status.HTTP_400_BAD_REQUEST)
            
            if coupon.per_user_daily_repeat <= user_daily_repeat:
                return Response({'message': "Daily repeat limit for this coupon for a user has been exceeded"}, status=status.HTTP_400_BAD_REQUEST)
            
            return Response({'message': "Coupon is valid and can be used"}, status=status.HTTP_200_OK)
        
        except Coupon.DoesNotExist:
            return Response({'message': "Coupon does not exist"}, status=status.HTTP_400_BAD_REQUEST)
        
        except User.DoesNotExist:
            return Response({'message': "User does not exist"}, status=status.HTTP_400_BAD_REQUEST)


class ApplyCoupon(APIView):
    def post(self, request):
        try:
            coupon_code = request.data.get('coupon_code')
            verification_url = 'http://localhost:8000/verify-validity/'
            verification_data = {'coupon_code': coupon_code}
            response = requests.post(verification_url, data=verification_data)
            if response.status_code == status.HTTP_200_OK:
                coupon = Coupon.objects.get(code=coupon_code)  
                repeat_count= RepeatCount.objects.create(coupon=coupon)
                repeat_count.save()
                serializer = RepeatCountSerializer(repeat_count)

                return Response({'message': "Coupon applied successfully",'data':serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({'message': "Coupon verification failed"}, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
