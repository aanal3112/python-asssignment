from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    global_total_repeat = models.IntegerField(default=0)
    per_user_total_repeat = models.IntegerField(default=0)
    per_user_daily_repeat = models.IntegerField(default = 0)
    per_user_weekly_repeat = models.IntegerField(default=0)
    

class RepeatCount(models.Model):
    coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)