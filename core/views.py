from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import * 
from .models import *   
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.views import View
# Create your views here.


def home(request):
    return render(request, "home.html")

def registro(request):
   
    datos = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            return redirect(to="home")
        datos["form"] = formulario

    return render(request, 'registration/registro.html', datos)
    from django.shortcuts import render, redirect, get_object_or_404


@login_required
def reserva_h(request):
    return HttpResponse('reserva_h.html')

    if request.method == 'POST':


        formulario = HabitacionForm(request.POST)
"""
    if 'habitacion' in request.GET: 'habitacion'
        habitacion_id = request.GET['habitacion']
        formulario.actualizar_horas_disponibles(habitacion_id)
        horas_disponibles = HoraDisponible.objects.filter(habitacion_id=habitacion_id)
          reserva = {"habitacion": request.POST['habitacion'],
                   "numero":request.POST['cantidad_camas'],
                   "cantidad_camas":request.POST['dia'],
                   "tipo_habitacion": request.POST['tipo_habitacion']}  
    
    datos['form'] = formulario
    datos['habitacion'] = Habitacion.objects.all()


from django.shortcuts import render, redirect, get_object_or_404

"""