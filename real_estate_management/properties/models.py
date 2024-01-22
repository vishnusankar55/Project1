# properties/models.py
from django.db import models

class Property(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    location = models.CharField(max_length=50)
    features = models.TextField()

    def __str__(self):
        return self.name

class Unit(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=[('1BHK', '1BHK'), ('2BHK', '2BHK'), ('3BHK', '3BHK')])
    rent_cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.property.name}'s {self.type} Unit"
