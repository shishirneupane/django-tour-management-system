from django.forms import ModelForm, SelectDateWidget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class GuestForm(ModelForm):
    class Meta:
        model = Guest
        fields = '__all__'
        widgets = {
            'arrival_date': SelectDateWidget(),
            'departure_date': SelectDateWidget()
        }