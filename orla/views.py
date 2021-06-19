from django.shortcuts import render
from django.http import HttpResponse
from orla.models import Curso, Profesor, Alumno, Orla
# Create your views here.
def orla_list(request,id_orla):    
    #curso = Curso.objects.filter(codigo='1')
    #profesores = Profesor.objects.filter(estado='activo')
    #alumnos = Alumno.objects.filter(estado='activo')

    orlas = Orla.objects.filter(codigo=id_orla)     # orla en forma de lista
    if orlas:
        orlaObject = Orla.objects.get(codigo=id_orla)   # orla como objeto
        alumnos = Alumno.objects.filter(curso=orlaObject.curso)
        profesores = Profesor.objects.filter(curso=orlaObject.curso)
        print(orlaObject)
        return render(request, 'orla.html', {'profesores': profesores,'alumnos': alumnos,'orla':orlaObject})
    else:
        return render(request, 'crearOrla.html')
    #if orlas.count() > 0:
    #return render(request, 'orla.html', {'curso': curso, 'profesores': profesores2,'alumnos': alumnos2,'orlas':orlas})
    #else: 
     #   return render(request, 'crearOrla.html')
        


    