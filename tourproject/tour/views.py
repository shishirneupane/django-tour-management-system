from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *
from ums.decorators import allowed_users

# Create your views here.

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'staff'])
def destinations(request):
    allDestinations = Destination.objects.all()
    form = DestinationForm()
    if request.method == 'POST':
        form = DestinationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('destinations')
    context = {'allDestinations': allDestinations, 'form': form}
    return render(request, 'tour/destinations.html', context=context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'staff'])
def hotels(request):
    allHotels = Hotel.objects.all()
    form = HotelForm()
    if request.method == 'POST':
        form = HotelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hotels')
    context = {'allHotels': allHotels, 'form': form}
    return render(request, 'tour/hotels.html', context=context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'staff'])
def airlines(request):
    allAirlines = Airline.objects.all()
    form = AirlineForm()
    if request.method == 'POST':
        form = AirlineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('airlines')
    context = {'allAirlines': allAirlines, 'form': form}
    return render(request, 'tour/airlines.html', context=context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteDestination(request, id):
    destination = Destination.objects.get(id=id)
    destination.delete()
    return redirect('destinations')


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteHotel(request, id):
    hotel = Hotel.objects.get(id=id)
    hotel.delete()
    return redirect('hotels')


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteAirline(request, id):
    airline = Airline.objects.get(id=id)
    airline.delete()
    return redirect('airlines')


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateDestination(request, id):
    destination = Destination.objects.get(id=id)
    form = DestinationForm(instance=destination)
    if request.method == 'POST':
        form = DestinationForm(request.POST, instance=destination)
        if form.is_valid():
            form.save()
            return redirect('destinations')
    return render(request, 'tour/update_form.html', context = {'form': form})
    

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateHotel(request, id):
    hotel = Hotel.objects.get(id=id)
    form = HotelForm(instance=hotel)
    if request.method == 'POST':
        form = HotelForm(request.POST, instance=hotel)
        if form.is_valid():
            form.save()
            return redirect('hotels')
    return render(request, 'tour/update_form.html', context = {'form': form})
    

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateAirline(request, id):
    airline = Airline.objects.get(id=id)
    form = AirlineForm(instance=airline)
    if request.method == 'POST':
        form = AirlineForm(request.POST, instance=airline)
        if form.is_valid():
            form.save()
            return redirect('airlines')
    return render(request, 'tour/update_form.html', context = {'form': form})