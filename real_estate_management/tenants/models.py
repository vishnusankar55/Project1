from django.db import models

class Tenant(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    document_proof = models.FileField(upload_to='tenant_documents/')

class RentalAgreement(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    unit = models.ForeignKey('properties.Unit', on_delete=models.CASCADE)
    agreement_end_date = models.DateField()
    monthly_rent_date = models.PositiveIntegerField()
