from django.forms import ModelForm
from .models import *


class DestinationForm(ModelForm):
    class Meta:
        model = Destination
        fields = '__all__'


class HotelForm(ModelForm):
    class Meta:
        model = Hotel
        fields = '__all__'


class AirlineForm(ModelForm):
    class Meta:
        model = Airline
        fields = '__all__'