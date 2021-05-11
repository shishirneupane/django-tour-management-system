from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class DateInput(forms.DateInput):
    input_type = 'date'


class GuestForm(ModelForm):
    class Meta:
        model = Guest
        fields = '__all__'
        widgets = {
            'arrival_date': DateInput(),
            'departure_date': DateInput()
        }