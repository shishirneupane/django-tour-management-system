from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from .forms import CreateUserForm, GuestForm
from .models import Guest
from tour.models import Destination, Airline, Hotel
from .decorators import unauthenticated_user, allowed_users
from .filters import GuestFilter

# Create your views here.

@login_required(login_url=login)
@allowed_users(allowed_roles=['admin'])
def add_staff(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            # add newly registered users to staff group
            group = Group.objects.get(name='staff')
            user.groups.add(group)
            messages.success(request, 'New staff added - \'' + username + '\'')
            return redirect('home')
    context = {'form': form}
    return render(request, 'ums/add_staff.html', context)


@unauthenticated_user
def register_page(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            # add newly registered users to staff group
            group = Group.objects.get(name='staff')
            user.groups.add(group)
            messages.success(request, 'New staff added - \'' + username + '\'')
            return redirect('home')
    context = {'form': form}
    return render(request, 'ums/register.html', context)


@unauthenticated_user
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')

    context = {}
    return render(request, 'ums/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'staff'])
def home(request):
    guest_count = Guest.objects.count()
    destination_count = Destination.objects.count()
    hotel_count = Hotel.objects.count()
    airline_count = Airline.objects.count()

    guests = Guest.objects.all()
    guestFilter = GuestFilter(request.GET, queryset=guests)
    guests = guestFilter.qs

    context = {
        'guest_count': guest_count,
        'destination_count': destination_count, 
        'hotel_count': hotel_count, 
        'airline_count': airline_count,
        'guests': guests,
        'guestFilter': guestFilter
    }
    return render(request, 'ums/dashboard.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'staff'])
def guests(request):
    guests = Guest.objects.all()
    context = {'guests': guests}
    return render(request, 'ums/guests.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'staff'])
def addGuest(request):
    form = GuestForm()
    if request.method == 'POST':
        form = GuestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('guests')
    context = {'form': form}
    return render(request, 'ums/add_guest.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'staff'])
def updateGuest(request, id):
    guest = Guest.objects.get(id=id)
    form = GuestForm(instance=guest)
    if request.method == 'POST':
        form = GuestForm(request.POST, instance=guest)
        if form.is_valid():
            form.save()
            return redirect('guests')
    context = {'form': form}
    return render(request, 'tour/update_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'staff'])
def deleteGuest(request, id):
    guest = Guest.objects.get(id=id)
    guest.delete()
    return redirect('guests')