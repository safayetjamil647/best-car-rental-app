from django.db import models

# Create your models here.
class Bookings(models.Model):
    price_id = models.SmallAutoField(primary_key=True)
    from_destination = models.CharField(max_length=50)
    to_destination = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    pick_up_date = models.DateField(auto_now=True, )
    pick_up_time = models.DateField(auto_now=True, )
    ordered_at = models.DateField(auto_now=True, )
    updated_at = models.DateField(auto_now=True, )
    deleted_at = models.DateField(auto_now=True, )