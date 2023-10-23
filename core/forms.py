from dataclasses import fields
from django import forms
from django.forms import ModelForm, DateInput
from .models import *

from datetime import datetime, timedelta
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class HabitacionForm(forms.ModelForm):
    class Meta:
        model = Habitacion
        fields = ['numero', 'cantidad_camas', 'tipo_habitacion']

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['nombres', 'apellidos', 'habitacion']


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]