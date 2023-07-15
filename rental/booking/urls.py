from django.urls import path
from . import views

app_name = 'bookings'

urlpatterns = [
    # other URL patterns
    path('booking/add/', views.add_booking, name='add_booking'),
    path('booking/list/', views.list_booking, name='booking_list'),
    path('booking/detail/<int:booking_id>/', views.detail_booking, name='booking_detail'),
    path('booking/remove/<int:booking_id>/', views.remove_booking, name='remove_booking'),
]