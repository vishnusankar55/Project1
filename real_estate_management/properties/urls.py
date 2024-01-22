# properties/urls.py
from django.urls import path
from .views import property_list, property_detail

urlpatterns = [
    path('properties/', property_list, name='property_list'),
    path('properties/<int:property_id>/', property_detail, name='property_detail'),
]
