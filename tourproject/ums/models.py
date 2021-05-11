from django.db import models
from tour.models import *

# Create your models here.

class Country(models.Model):
    countryName = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.countryName


class Guest(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    country = models.ForeignKey(Country, null=True, on_delete=models.SET_NULL)
    arrival_date = models.DateField(null=True)
    departure_date = models.DateField(null=True)
    destination = models.ForeignKey(Destination, null=True, on_delete=models.SET_NULL)
    hotel = models.ForeignKey(Hotel, null=True, on_delete=models.SET_NULL)
    airline = models.ForeignKey(Airline, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.name
