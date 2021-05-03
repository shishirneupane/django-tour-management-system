from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm, GuestForm
from .models import Guest
from .decorators import unauthenticated_user, allowed_users

# Create your views here.

@unauthenticated_user
def register_page(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')

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
    context = {}
    return render(request, 'ums/dashboard.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'staff'])
def guests(request):
    guests = Guest.objects.all()
    form = GuestForm()
    if request.method == 'POST':
        form = GuestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('guests')
    context = {'guests': guests, 'form': form}
    return render(request, 'ums/guests.html', context)


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
    context = {'guest': guest}
    return render(request, 'tour/guests.html', context)