from django.urls import path
from . import views

urlpatterns = [
    path('treks/', views.treks, name='treks'),
]
