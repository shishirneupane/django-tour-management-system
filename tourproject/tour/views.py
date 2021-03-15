from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *

# Create your views here.

@login_required(login_url='login')
def destinations(request):
    allDestinations = Destination.objects.all()
    form = DestinationForm()
    if request.method == 'POST':
        form = DestinationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('destinations')
    context = {'allDestinations': allDestinations, 'form': form}
    return render(request, 'tour/destinations.html', context)


@login_required(login_url='login')
def hotels(request):
    allHotels = Hotel.objects.all()
    form = HotelForm()
    if request.method == 'POST':
        form = HotelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hotels')
    context = {'allHotels': allHotels, 'form': form}
    return render(request, 'tour/hotels.html', context)


@login_required(login_url='login')
def airlines(request):
    allAirlines = Airline.objects.all()
    form = AirlineForm()
    if request.method == 'POST':
        form = AirlineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('airlines')
    context = {'allAirlines': allAirlines, 'form': form}
    return render(request, 'tour/airlines.html', context)