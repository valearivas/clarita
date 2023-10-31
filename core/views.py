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


def addProveedor(request):
    data = {
        'form' : ProveedorForm()
    }
    if request.method == 'POST':
        formulario = ProveedorForm(request.POST)
        
        if formulario.is_valid:
            formulario.save()
            data['mensaje'] = 'Guardado exitosamente'

    return render(request,'proveedores/addProveedor.html', data)




def registroCliente(request):

    data = {
        'form': clienteForm()
    }

    if request.method == 'POST':
        formulario = clienteForm(data=request.POST)
        if formulario.is_valid():
            empresa = formulario.save(commit=False)
            empresa.es_cliente = True  # Establece el campo es_cliente en la instancia del modelo
            empresa.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            print("Registro guardado exitosamente")
            return redirect('home') 

    return render(request, 'registration/registroCliente.html', data)


def registroEmpleado(request):

    data = {
        'form': EmpleadoForm()
    }

    if request.method == 'POST':
        formulario = EmpleadoForm(data=request.POST)
        if formulario.is_valid():
            empresa = formulario.save(commit=False)
            empresa.nombre_empresa == "Doña Clarita"
            empresa.es_empleado = True  
            empresa.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            print("Registro guardado exitosamente")
            return redirect('home') 

    return render(request, 'registration/registroEmpleado.html', data)





def readProveedor(request):
    proveedor = Proveedor.objects.all()
    data = {
        'proveedor': proveedor
    }
    return render (request, 'proveedores/readProveedor.html', data)


def readCliente(request):
    clientes = Usuario.objects.filter(cliente = Usuario.es_cliente == True)

    data = {
        'cliente': clientes
    }
    return render (request, 'proveedores/readProveedor.html', data)


def perfilCliente(request):
    

    return render(request, 'clientes/perfilCliente.html')


def eliminarProveedor(request, id):
    proveedor = Proveedor.objects.get(id=id)

    if request.method == 'POST':
        proveedor.delete()
        return redirect('readProveedor')

    return render(request, 'proveedores/eliminarProveedor.html', {'proveedor': proveedor})


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