from django.urls import path, reverse

from wagtail.admin.menu import Menu, MenuItem, SubmenuMenuItem
from wagtail import hooks

from .views import list_booking


@hooks.register('register_admin_urls')
def register_booking_url():
    return [
        path('booking/list/', list_booking, name='booking_list'),
        
    ]


@hooks.register('register_admin_menu_item')
def register_booking_menu_item():
    submenu = Menu(items=[
        MenuItem('Rides', reverse('booking_list'), icon_name='date'),
    ])

    return SubmenuMenuItem('Bookings', submenu, icon_name='date')