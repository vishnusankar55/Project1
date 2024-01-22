# properties/views.py
from django.shortcuts import render
from .models import Property, Unit

def property_list(request):
    properties_list = Property.objects.all()
    return render(request, 'properties/property_list.html', {'properties_list': properties_list})

def property_detail(request, property_id):
    property_item = Property.objects.get(pk=property_id)
    units = Unit.objects.filter(property=property_item)
    return render(request, 'properties/property_detail.html', {'property': property_item, 'units': units})
