from django.db import models
from cars.models import Car
# Create your models here.
class Pricing(models.Model):
    car_name = models.CharField(max_length=30,null=True)
    price_hourly = models.CharField(max_length=8)
    price_daily = models.CharField(max_length=8)
    price_leasing  = models.CharField(max_length=8)
    created_at = models.DateField(auto_now=True, )
    updated_at = models.DateField(auto_now=True, )