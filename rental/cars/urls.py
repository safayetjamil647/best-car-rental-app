from django.urls import path

from .views import all_cars,add_cars,remove_cars,details_car,update_cars
app_name = "cars"
urlpatterns = [
    path('cars/', all_cars, name='cars'),
    path('cars/add/', add_cars, name='add_cars'),
    path('cars/details/<int:car_id>/', details_car, name='details_car'),
    path('cars/remove/<int:car_id>/', remove_cars, name='remove_car'),
    path('cars/update/<int:car_id>/', update_cars, name='update_car'),


]