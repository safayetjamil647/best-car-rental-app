from django.shortcuts import render, redirect,  get_object_or_404
from .forms import CarForm
from .models import Car
# Create your views here.
def all_cars(request):
    cars = Car.objects.all()
    return render(request, 'all_cars/index.html', {'cars': cars})
    

def add_cars(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/admin/cars/all/')
    else:
        form = CarForm()
    return render(request, 'add_car/index.html', {'form': form})


def details_car(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    return render(request, 'details_car/index.html', {'car': car})


def remove_cars(request, car_id):
      car = get_object_or_404(Car, pk=car_id)
      car.delete()
      return redirect('cars:cars')
    

def update_cars(request,car_id):
    car = get_object_or_404(Car, pk=car_id)
    
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            form.save()
            return redirect('cars:details_car', car_id=car_id)
    else:
        form = CarForm(instance=car)
    
    return render(request, 'update_car/index.html', {'form': form, 'car': car})