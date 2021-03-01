from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import TrekDestination

# Create your views here.

@login_required(login_url='login')
def treks(request):
    treks = TrekDestination.objects.all()
    context = {'treks': treks}
    return render(request, 'tour/treks.html', context)