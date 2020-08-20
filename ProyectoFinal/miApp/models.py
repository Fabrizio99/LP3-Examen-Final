from django.db import models

class Curso(models.Model):
    idcurso =  models.AutoField(primary_key=True)
    codigo  =  models.TextField()
    nombre  =  models.TextField()
    horas   =  models.TextField()
    creditos = models.TextField()
    estado  =  models.CharField(max_length=1)

class Carrera(models.Model):
    idcarrera =  models.AutoField(primary_key=True)
    nombre  =  models.TextField()
    nombrecorto   =  models.TextField()
    fecha_fundacion = models.DateTimeField()
    estado  =  models.CharField(max_length=1)