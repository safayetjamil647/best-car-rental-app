from django.urls import path, reverse

from wagtail.admin.menu import Menu, MenuItem, SubmenuMenuItem
from wagtail import hooks

from .views import add_pricing,remove_pricing


@hooks.register('register_admin_urls')
def register_calendar_url():
    return [
        path('pricing/add/', add_pricing, name='add_pricing'),
        path('pricing/remove/', remove_pricing, name='remove_pricing'),
    ]


@hooks.register('register_admin_menu_item')
def register_calendar_menu_item():
    submenu = Menu(items=[
        MenuItem('Add Price', reverse('add_pricing'), icon_name='date'),
        MenuItem('Remove Pricing', reverse('remove_pricing'), icon_name='date'),
    ])

    return SubmenuMenuItem('Pricing', submenu, icon_name='date')