from django.urls import path
from .views import *
from . import views


urlpatterns = [
    path('', home, name="home"),
    path('login/', login, name='login'),
    path('registro/', registro, name="registro"),
    path('reserva_h/', reserva_h, name="reserva_h")
    ]