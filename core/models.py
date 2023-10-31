from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime


class Usuario(AbstractUser):
    es_cliente = models.BooleanField(default=False)
    es_empleado = models.BooleanField(default=False)
    nombre_empresa = models.CharField(max_length=100, blank=True, null=True)
    rut_empresa = models.CharField(max_length=15)
    cargo = models.CharField(max_length=100, blank=True, null=True)
    imagen = models.ImageField(upload_to="iconoUsuario", default= "user.png")

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['-id']

    def __str__(self):
        return f"{self.nombre_empresa} {self.rut_empresa} {self.cargo}"


class Habitacion(models.Model):
    DISPONIBILIDAD_CHOICES = (
        ('Disponible', 'Disponible'),
        ('No disponible por estar asignada a empresa', 'No disponible por estar asignada a empresa'),
        ('No disponible por estar en mantenimiento', 'No disponible por estar en mantenimiento'),
    )
    n_habitacion = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=30)
    precio = models.IntegerField()
    n_camas = models.IntegerField()
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="habitaciones", null=True)
    estado_habitacion = models.CharField(max_length=50, choices=DISPONIBILIDAD_CHOICES)

    class Meta:
        verbose_name = 'Habitacion'
        verbose_name_plural = 'Habitaciones'

    def __str__(self):
        return f"{self.n_habitacion} {self.nombre}"


class ServicioComedor(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Tipo_servicio'
        verbose_name_plural = 'Tipo_servicios'

    def __str__(self):
        return f"{self.nombre}"


class Comedor(models.Model):
    nombre_plato = models.CharField(max_length=30)
    precio = models.IntegerField()
    servicio_comedor = models.ForeignKey(ServicioComedor, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Comedor'
        verbose_name_plural = 'Comedores'

    def __str__(self):
        return f"{self.nombre_plato} {self.precio} {self.servicio_comedor}"


class Huesped(models.Model):
    nombre_huesped = models.CharField(max_length=80)
    nombre_empresa = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    habitacion_asignada = models.ForeignKey(Habitacion, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Huesped'
        verbose_name_plural = 'Huespedes'

    def __str__(self):
        return f"{self.nombre_huesped} {self.nombre_empresa} {self.habitacion_asignada}"


class Empleado(models.Model):
    nombre = models.CharField(max_length=80)
    cargo = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def __str__(self):
        return f"{self.nombre} {self.cargo}"


class OrdenCompra(models.Model):
    numero_orden = models.CharField(max_length=10, unique=True)
    empresa = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_actual = datetime.date.today()
    fecha_check_in = models.DateField()
    fecha_check_out = models.DateField()
    habitaciones_asociadas = models.ManyToManyField(Habitacion)
    servicios_adicionales = models.ManyToManyField(Comedor)
    huesped = models.ManyToManyField(Huesped)
    detalle_reserva = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Orden_compra'
        verbose_name_plural = 'Ordenes_compra'

    def __str__(self):
        return f"{self.empresa} {self.huesped} {self.fecha_check_in} {self.fecha_check_out}"

    def calcular_precio_total(self):
        precio_total = 0

        for habitacion in self.habitaciones_asociadas.all():
            precio_total += habitacion.precio

        for servicio in self.servicios_adicionales.all():
            precio_total += servicio.precio

        return precio_total


class Proveedor(models.Model):
    nombre = models.CharField(max_length=80)
    rubro = models.CharField(max_length=30)
    contacto = models.IntegerField()
    otro = models.TextField()

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'

    def __str__(self):
        return f"{self.nombre} {self.rubro} {self.contacto} {self.otro}"
