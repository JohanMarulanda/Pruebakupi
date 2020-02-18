from django.db import models

# Create your models here.


class cliente(models.Model):
    id = models.AutoField(primary_key=True)
    cedula = models.IntegerField(default=0)
    nombre = models.CharField(max_length=255, default='')
    telefono = models.IntegerField(default=0)
    correo = models.CharField(max_length=255, default='')
    ciudad = models.CharField(max_length=100, default='')

    class Meta: 
        db_table = 'usuarios_cliente'

class ciudad(models.Model):
    idCiudad = models.IntegerField(default=0)
    nomCiudad = models.CharField(max_length=255, default='')
    idDepartamento = models.IntegerField(default=0)

    class Meta:
        db_table = 'usuarios_cuidad'


class departamento(models.Model):
    idDepartamento = models.IntegerField(default=0)
    nomDepartamento = models.CharField(max_length=255, default='')

    class Meta:
        db_table = 'usuarios_departamento'
