from django.urls import path
from . import views

urlpatterns = [
    path('destinations/', views.destinations, name='destinations'),
    path('hotels/', views.hotels, name='hotels'),
    path('airlines/', views.airlines, name='airlines'),
]