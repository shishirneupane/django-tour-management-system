from django.shortcuts import render, redirect

# Create your views here.

def home(request):
    context = {}
    return render(request, 'ums/dashboard.html', context)


def register_page(request):
    context = {}
    return render(request, 'ums/register.html', context)
    

def login_page(request):
    context = {}
    return render(request, 'ums/login.html', context)
