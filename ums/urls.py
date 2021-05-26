from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_staff/', views.add_staff, name='add_staff'),
    path('register/', views.register_page, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('bookings/', views.guests, name='guests'),
    path('new_booking/', views.addGuest, name='add_guest'),
    path('delete_guest/<int:id>/', views.deleteGuest, name='delete_guest'),
    path('update_guest/<int:id>/', views.updateGuest, name='update_guest'),
]
