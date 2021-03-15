from django.db import models

# Create your models here.

class Destination(models.Model):
    destinationName = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.destinationName


class Airline(models.Model):
    airlineName = models.CharField(max_length=200, null=True)
    fare = models.FloatField(max_length=200, null=True)
    def __str__(self):
        return self.airlineName


class Hotel(models.Model):
    hotelName = models.CharField(max_length=200, null=True)
    fare = models.FloatField(max_length=200, null=True)
    def __str__(self):
        return self.hotelName