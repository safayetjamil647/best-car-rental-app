from django.urls import path
from . import views
app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('cars/', views.cars, name='cars'),
    path('pricing/', views.pricings, name='pricings'),
    path('contact/', views.contact, name='contact'),
    path('cars/', views.car_list, name='car_list'),
]