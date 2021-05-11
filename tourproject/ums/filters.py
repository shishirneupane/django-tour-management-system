import django_filters
from .models import Guest


class GuestFilter(django_filters.FilterSet):
    class Meta:
        model = Guest
        fields = ['country', 'destination', 'hotel', 'airline', 'arrival_date', 'departure_date']