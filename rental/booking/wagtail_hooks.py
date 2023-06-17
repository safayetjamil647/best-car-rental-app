from django.urls import path, reverse

from wagtail.admin.menu import Menu, MenuItem, SubmenuMenuItem
from wagtail import hooks

from .views import booking,routes


@hooks.register('register_admin_urls')
def register_calendar_url():
    return [
        path('routes/index/', booking, name='routes'),
        path('rides/index/', routes, name='rides'),
    ]


@hooks.register('register_admin_menu_item')
def register_calendar_menu_item():
    submenu = Menu(items=[
        MenuItem('Routes', reverse('routes'), icon_name='date'),
        MenuItem('Rides', reverse('rides'), icon_name='date'),
    ])

    return SubmenuMenuItem('Bookings', submenu, icon_name='date')