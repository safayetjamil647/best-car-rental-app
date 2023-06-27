from django.shortcuts import render

# Create your views here.
def all_cars(request):
    return render(request, 'all_cars/index.html')

def add_cars(request):
    return render(request, 'add_car/index.html')

def details_car(request):
    return render(request, 'details_car/index.html')

def remove_cars(request):
    return render(request, 'remove_car/index.html')

def update_cars(request):
    return render(request, 'all_cars/index.html')