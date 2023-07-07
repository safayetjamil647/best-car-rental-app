from django.urls import path, reverse

from wagtail.admin.menu import Menu, MenuItem, SubmenuMenuItem
from wagtail import hooks

from .views import all_cars,add_cars,remove_cars,details_car


@hooks.register('register_admin_urls')
def register_car_url():
    return [
        path('cars/all/', all_cars, name='all_cars'),
        path('cars/add/', add_cars, name='add_cars'),
        
        
        
    ]


@hooks.register('register_admin_menu_item')
def register_car_menu_item():
    submenu = Menu(items=[
        MenuItem('Manage Cars', reverse('all_cars'), icon_name='date'),
        MenuItem('Third Party Car', reverse('add_cars'), icon_name='date'),
       
    ])

    return SubmenuMenuItem('Car Manager', submenu, icon_name='date')