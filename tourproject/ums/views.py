from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import CreateUserForm

# Create your views here.

def home(request):
    context = {}
    return render(request, 'ums/dashboard.html', context)


def register_page(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')

    context = {'form': form}
    return render(request, 'ums/register.html', context)
    

def login_page(request):
    context = {}
    return render(request, 'ums/login.html', context)
