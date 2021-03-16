from django.urls import path
from . import views

urlpatterns = [
    path('destinations/', views.destinations, name='destinations'),
    path('hotels/', views.hotels, name='hotels'),
    path('airlines/', views.airlines, name='airlines'),
    path('delete_destination/<int:id>/', views.deleteDestination, name='delete_destination'),
    path('delete_hotel/<int:id>/', views.deleteHotel, name='delete_hotel'),
    path('delete_airline/<int:id>/', views.deleteAirline, name='delete_airline'),
]