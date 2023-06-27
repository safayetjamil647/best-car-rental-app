from django.urls import path, reverse

from wagtail.admin.menu import Menu, MenuItem, SubmenuMenuItem
from wagtail import hooks

from .views import all_cars,add_cars,remove_cars


@hooks.register('register_admin_urls')
def register_calendar_url():
    return [
        path('cars/all/', all_cars, name='all_cars'),
        path('cars/add/', add_cars, name='add_cars'),
        path('cars/remove/', remove_cars, name='remove_cars'),
    ]


@hooks.register('register_admin_menu_item')
def register_calendar_menu_item():
    submenu = Menu(items=[
        MenuItem('All Car', reverse('all_cars'), icon_name='date'),
        MenuItem('Add Car', reverse('add_cars'), icon_name='date'),
        MenuItem('Remove Car', reverse('remove_cars'), icon_name='date'),
    ])

    return SubmenuMenuItem('Cars', submenu, icon_name='date')