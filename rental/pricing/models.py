from django.db import models

# Create your models here.
class Pricing(models.Model):
    price_id = models.SmallAutoField(primary_key=True)
    price_hourly = models.CharField(max_length=50)
    price_daily = models.CharField(max_length=50)
    price_leasing  = models.CharField(max_length=50)
    created_at = models.DateField(auto_now=True, )
    updated_at = models.DateField(auto_now=True, )