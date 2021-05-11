import django_filters
from .models import *
from tour.models import *
from .forms import DateInput


class GuestFilter(django_filters.FilterSet):
	class Meta:
		model = Guest
		fields = ['country', 'destination', 'hotel', 'airline', 'arrival_date', 'departure_date']
		widgets = {
            'arrival_date': DateInput(),
            'departure_date': DateInput()
        }