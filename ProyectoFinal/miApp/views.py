from django.shortcuts import render,HttpResponse,redirect
from miApp.models import Curso

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
    return render(request,'listar_carreras.html',
        {         'titulo' : 'CARRERAS','mensaje' : 'LISTADO DE CARRERAS' })


def listar_estudiantes(request):
    return render(request,'listar_estudiantes.html',
        {         'titulo' : 'ESTUDIANTES','mensaje' : 'LISTADO DE ESTUDIANTES'   })



def listar_consultas(request):
    return render(request,'listar_consultas.html',
    {         'titulo' : 'CONSULTAS','mensaje' : 'CONSULTAS Y COMENTARIOS'   })

def eliminar_curso(request, id):     
    curso = Curso.objects.get(pk=id)     
    curso.delete()     
    return redirect('listarCurso')