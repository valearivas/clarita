from django.urls import path
from .views import *
from . import views


urlpatterns = [
    path('', home, name="home"),
    path('login/', login, name='login'),
    path('registro/', registro, name="registro"),
    path('registroCliente/', registroCliente, name='registroCliente'),
    path('registroEmpleado/', registroEmpleado, name='registroEmpleado'),
    path('addProveedor/', addProveedor, name='addProveedor'),
    path('readProveedor/', readProveedor, name='readProveedor'),
    path('eliminarProveedor/<id>/',eliminarProveedor,name='eliminarProveedor'),
    ]