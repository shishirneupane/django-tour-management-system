from django.db import models
from tour.models import *

# Create your models here.

class Guest(models.Model):
    COUNTRY_CHOICES = (
        ('Nepal', 'Nepal'),
        ('Japan', 'Japan'),
        ('China', 'China'),
        ('India', 'India'),
        ('USA', 'USA'),
        ('Germany', 'Germany'),
        ('Thailand', 'Thailand'),
    )
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    country = models.CharField(max_length=200, null=True, choices=COUNTRY_CHOICES)
    destination = models.ForeignKey(Destination, null=True, on_delete=models.SET_NULL)
    hotel = models.ForeignKey(Hotel, null=True, on_delete=models.SET_NULL)
    airline = models.ForeignKey(Airline, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
