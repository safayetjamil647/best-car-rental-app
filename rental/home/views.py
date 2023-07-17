from django.shortcuts import render
from cars.models import Car
def index(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about.html')

def services(request):
    return render(request, 'home/services.html')

def pricings(request):
    return render(request, 'home/pricing.html')

def cars(request):
    return render(request, 'home/cars.html')
def car_list(request):
    cars = Car.objects.all()
    return render(request, 'home/cars.html', {'cars': cars})
def contact(request):
    return render(request, 'home/contact.html')