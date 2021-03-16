from django.urls import path
from . import views

urlpatterns = [
    path('destinations/', views.destinations, name='destinations'),
    path('hotels/', views.hotels, name='hotels'),
    path('airlines/', views.airlines, name='airlines'),
    path('delete_destination/<int:id>/', views.deleteDestination, name='delete_destination'),
    path('delete_hotel/<int:id>/', views.deleteHotel, name='delete_hotel'),
    path('delete_airline/<int:id>/', views.deleteAirline, name='delete_airline'),
    path('update_destination/<int:id>/', views.updateDestination, name='update_destination'),
    path('update_hotel/<int:id>/', views.updateHotel, name='update_hotel'),
    path('update_airline/<int:id>/', views.updateAirline, name='update_airline'),
]