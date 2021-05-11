from django.forms import widgets
from django.forms.widgets import Select
import django_filters
from django.forms import SelectDateWidget
from .models import *


class GuestFilter(django_filters.FilterSet):
    class Meta:
        model = Guest
        fields = ['country', 'destination', 'hotel', 'airline', 'arrival_date', 'departure_date']