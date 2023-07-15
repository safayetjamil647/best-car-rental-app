from django.db import models

# Create your models here.
class Car(models.Model):
    TRANSMISSION = [
        ("A", "Auto"),
        ("M", "Manual"),
    ]
    FUEL = [
        ("P","Petrol"),
        ("O","Octane"),
        ("E","Electric")
    ]
    Seats = [
        ("3", "3 Adults"),
        ("4", "4 Adults"),
        ("5", "5 Adults"),
    ]
    Luggage = [
        ("2", "2 Bags"),
        ("3", "3 Bags"),
        ("4", "4 Bags"),
    ]


    car_name = models.CharField(max_length=50)
    car_registration = models.TextField(max_length=20) 
    car_description = models.TextField(max_length=250)
    car_mileage  = models.CharField(max_length=8)
    car_transmission  = models.CharField(max_length=8,choices=TRANSMISSION)
    car_seats = models.CharField(max_length=10,choices=Seats)
    car_luggage = models.CharField(max_length=10,choices=Luggage)
    car_fuel = models.CharField(max_length=10,choices=FUEL)
    car_images = models.ImageField(upload_to="cars_image")
    available_now = models.BooleanField(default=True)
    created_at = models.DateField(auto_now=True, )
    updated_at = models.DateField(auto_now=True, )