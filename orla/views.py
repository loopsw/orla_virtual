from django.shortcuts import render
from orla.models import Curso, Profesor, Alumno, Orla
# Create your views here.
def orla_list(request,id_orla):
    curso = Curso.objects.filter(codigo='1')
    profesores = Profesor.objects.filter(estado='activo')
    alumnos = Alumno.objects.filter(estado='activo')
    orlas = Orla.objects.filter(codigo=id_orla)
    if orlas.count() > 0:
        return render(request, 'orla.html', {'curso': curso, 'profesores': profesores,'alumnos': alumnos,'orlas':orlas})
    else: 
        return render(request, 'crearOrla.html')
        


    