from django.db import models
from cars.models import Car
# Create your models here.
class Bookings(models.Model):
    PriceType = [
        ("Leasing", "L"),
        ("Hourly", "H"),
        ("Daily", "D"),
    ]
    car = models.CharField(max_length=50)
    from_destination = models.CharField(max_length=50)
    to_destination = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    price_type = models.CharField(max_length=8,choices=PriceType)
    pick_up_date = models.DateField()
    pick_up_time = models.DateField()
    end_time = models.DateField()
    ordered_at = models.DateField(auto_now=True, )
    updated_at = models.DateField(auto_now=True, )
    deleted_at = models.DateField(auto_now=True, )