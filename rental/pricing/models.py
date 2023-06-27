from django.db import models
from cars.models import Car
# Create your models here.
class Pricing(models.Model):
    car = models.OneToOneField(Car, on_delete=models.CASCADE, primary_key=True)
    price_hourly = models.CharField(max_length=50)
    price_daily = models.CharField(max_length=50)
    price_leasing  = models.CharField(max_length=50)
    created_at = models.DateField(auto_now=True, )
    updated_at = models.DateField(auto_now=True, )