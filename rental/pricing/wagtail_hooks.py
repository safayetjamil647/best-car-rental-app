from django.urls import path, reverse

from wagtail.admin.menu import Menu, MenuItem, SubmenuMenuItem
from wagtail import hooks

from .views import list_pricing


@hooks.register('register_admin_urls')
def register_pricing_url():
    return [
        path('pricing/', list_pricing, name='list_pricing'),
        
    ]


@hooks.register('register_admin_menu_item')
def register_pricing_menu_item():
    submenu = Menu(items=[
        MenuItem('Manage Price', reverse('list_pricing'), icon_name='date'),
        
    ])

    return SubmenuMenuItem('Price Manager', submenu, icon_name='date')