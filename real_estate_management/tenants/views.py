# tenants/views.py
from django.shortcuts import render
from .models import Tenant, RentalAgreement  # Import Tenant and RentalAgreement from the same module

def tenant_list(request):
    tenants_list = Tenant.objects.all()
    return render(request, 'tenants/tenants.html', {'tenants_list': tenants_list})

def tenant_detail(request, tenant_id):
    tenant_item = Tenant.objects.get(pk=tenant_id)
    agreements = RentalAgreement.objects.filter(tenant=tenant_item)
    return render(request, 'tenants/tenant_details.html', {'tenant': tenant_item, 'agreements': agreements})
