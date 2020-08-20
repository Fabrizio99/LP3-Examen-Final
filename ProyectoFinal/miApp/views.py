from django.shortcuts import render,HttpResponse,redirect
from miApp.models import Curso 
from miApp.models import Carrera
from miApp.models import Estudiante 

# Create your views here.
def index(request):     return render(request,'index.html',
    {         'titulo' : 'Inicio' ,'mensaje' : 'PAGINA DE INICIO'  }) 

def listar_cursos(request):
    cursos = Curso.objects.all()        

    return render(request,'listar_cursos.html',
        {       'titulo'  : 'CURSOS',
                'mensaje' : 'LISTADO DE CURSOS',
                'cursos'  : cursos
          })


def listar_carreras(request):
    carreras = Carrera.objects.all()
    return render(request,'listar_carreras.html',
        {         'titulo' : 'CARRERAS',
                'mensaje' : 'LISTADO DE CARRERAS',
                'carreras': carreras })


def listar_estudiantes(request):
    estudiantes = Estudiante.objects.all() 
    return render(request,'listar_estudiantes.html',
        {         'titulo' : 'ESTUDIANTES',
        'mensaje' : 'LISTADO DE ESTUDIANTES',
        'estudiantes': estudiantes   })



def listar_consultas(request):
    return render(request,'listar_consultas.html',
    {         'titulo' : 'CONSULTAS','mensaje' : 'CONSULTAS Y COMENTARIOS'   })

def eliminar_curso(request, id):     
    curso = Curso.objects.get(pk=id)     
    curso.delete()     
    return redirect('listarCurso')

def eliminar_carrera(request, id):     
    carrera = Carrera.objects.get(pk=id)     
    carrera.delete()     
    return redirect('listarCarrera')

def eliminar_estudiante(request, id):     
    estudiante = Estudiante.objects.get(pk=id)     
    estudiante.delete()     
    return redirect('listarEstudiantes')