# inventory/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inventory_list, name='inventory_list'),
    path('inventory', views.inventory_list, name='inventory_list'),
    path('inventory/<int:id>/', views.inventory_detail, name='inventory_detail'),
    path('api/inventory/', views.inventory_api, name='inventory_api'),
]
