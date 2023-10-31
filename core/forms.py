from dataclasses import fields
from django import forms
from django.forms import ModelForm, DateInput
from .models import *

from datetime import datetime, timedelta
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]

class clienteForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = [ "username" ,"nombre_empresa", "rut_empresa", "email", "password1", "password2"]


class EmpleadoForm(UserCreationForm):
     class Meta:
        model = Usuario
        fields = [ "username" ,"first_name","last_name" , "cargo", "email", "password1", "password2"]

class ProveedorForm(forms.ModelForm):
    class Meta: 
        model = Proveedor
        fields = ['nombre', 'rubro', 'contacto', 'otro']