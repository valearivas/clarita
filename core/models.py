from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

class Habitacion(models.Model):
    numero = models.IntegerField(verbose_name='NUMERO')
    cantidad_camas = models.CharField(max_length=50, verbose_name='CANTIDAD_CAMAS')
    tipo_habitacion = models.CharField(max_length=50, verbose_name='TIPO_HABITACION')

    def __str__(self):
        return f"{self.numero} {self.cantidad_camas} {self.tipo_habitacion}"

class Reserva(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE, verbose_name='HABITACION')

    def __str__(self):
        return f"{self.nombres} {self.apellidos} {self.habitacion}"

HORAS_DISPONIBLES = [
    ('08:00', '08:00 AM'), ('09:00', '09:00 AM'), ('10:00', '10:00 AM'),
    ('11:00', '11:00 AM'), ('12:00', '12:00 PM'), ('13:00', '01:00 PM'),
    ('14:00', '02:00 PM'), ('15:00', '03:00 PM'), ('16:00', '04:00 PM'), ('17:00', '05:00 PM')
]

class HoraDisponible(models.Model):
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE, related_name='horas_disponibles')
    dia = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True, verbose_name='dia')
    hora = models.CharField(choices=HORAS_DISPONIBLES, max_length=5, null=True, blank=True)

    def __str__(self):
        return f"{self.habitacion} {self.dia} {self.hora}"

