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


@login_required(login_url='login')
def deleteDestination(request, id):
    destination = Destination.objects.get(id=id)
    if request.method == 'POST':
        destination.delete()
        return redirect('destinations')
    context = {'destination': destination}
    return render(request, 'tour/destinations.html', context)


@login_required(login_url='login')
def deleteHotel(request, id):
    hotel = Hotel.objects.get(id=id)
    if request.method == 'POST':
        hotel.delete()
        return redirect('hotels')
    context = {'hotel': hotel}
    return render(request, 'tour/hotels.html', context)


@login_required(login_url='login')
def deleteAirline(request, id):
    airline = Airline.objects.get(id=id)
    if request.method == 'POST':
        airline.delete()
        return redirect('airlines')
    context = {'airline': airline}
    return render(request, 'tour/airlines.html', context)


@login_required(login_url='login')
def updateDestination(request, id):
    allDestinations = Destination.objects.all()
    destination = Destination.objects.get(id=id)
    form = DestinationForm(instance=destination)
    if request.method == 'POST':
        form = DestinationForm(request.POST, instance=destination)
        if form.is_valid():
            form.save()
            return redirect('destinations')
    context = {'allDestinations': allDestinations, 'form': form}
    return render(request, 'tour/destinations.html', context)
    

@login_required(login_url='login')
def updateHotel(request, id):
    allHotels = Hotel.objects.all()
    hotel = Hotel.objects.get(id=id)
    form = HotelForm(instance=hotel)
    if request.method == 'POST':
        form = HotelForm(request.POST, instance=hotel)
        if form.is_valid():
            form.save()
            return redirect('hotels')
    context = {'allHotels': allHotels, 'form': form}
    return render(request, 'tour/hotels.html', context)
    

@login_required(login_url='login')
def updateAirline(request, id):
    allAirlines = Airline.objects.all()
    airline = Airline.objects.get(id=id)
    form = AirlineForm(instance=airline)
    if request.method == 'POST':
        form = AirlineForm(request.POST, instance=airline)
        if form.is_valid():
            form.save()
            return redirect('airlines')
    context = {'allAirlines': allAirlines, 'form': form}
    return render(request, 'tour/airlines.html', context)