from django.urls import path
from . import views

app_name = 'pricing'

urlpatterns = [
    path('pricing/', views.list_pricing, name='list_pricing'),
    path('pricing/add', views.add_pricing, name='add_pricing'),
    path('pricing/detail/<int:pricing_id>/', views.detail_pricing, name='detail_pricing'),
    path('pricing/update/<int:pricing_id>/', views.update_pricing, name='update_pricing'),
    path('pricing/remove/<int:pricing_id>/', views.remove_pricing, name='remove_pricing'),
    # path('add/<int:car_id>/', views.add_pricing, name='add_pricing'),
]