from django.db import models

class Curso(models.Model):
    idcurso =  models.AutoField(primary_key=True)
    codigo  =  models.TextField()
    nombre  =  models.TextField()
    horas   =  models.TextField()
    creditos = models.TextField()
    estado  =  models.CharField(max_length=1)
