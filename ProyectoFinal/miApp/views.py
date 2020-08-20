from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def index(request):     return render(request,'index.html',
    {         'titulo' : 'Inicio' ,'mensaje' : 'PAGINA DE INICIO'  }) 

def listar_cursos(request):
    return render(request,'listar_cursos.html',
        {         'titulo' : 'CURSOS','mensaje' : 'LISTADO DE CURSOS'  })


def listar_carreras(request):
    return render(request,'listar_carreras.html',
        {         'titulo' : 'CARRERAS','mensaje' : 'LISTADO DE CARRERAS' })


def listar_estudiantes(request):
    return render(request,'listar_estudiantes.html',
        {         'titulo' : 'ESTUDIANTES','mensaje' : 'LISTADO DE ESTUDIANTES'   })



def listar_consultas(request):
    return render(request,'listar_consultas.html',
    {         'titulo' : 'CONSULTAS','mensaje' : 'CONSULTAS Y COMENTARIOS'   })