# serializers.py

from rest_framework import serializers
from .models import Coupon, RepeatCount
from django.contrib.auth.models import *

class UserSerilalizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username']


class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = ['id','code','per_user_daily_repeat','per_user_weekly_repeat','per_user_total_repeat','global_total_repeat']

class RepeatCountSerializer(serializers.ModelSerializer):
    coupon = CouponSerializer()
    
    class Meta:
        model = RepeatCount
        fields = ['coupon','created_at']
    
