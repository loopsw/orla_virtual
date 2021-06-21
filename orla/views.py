from django.shortcuts import render,redirect
from orla.forms import FormularioContacto
from django.core.mail import send_mail, BadHeaderError
from orla.models import Curso, Profesor, Alumno, Orla
# Create your views here.
def orla_list(request,id_orla):    
    #curso = Curso.objects.filter(codigo='1')
    #profesores = Profesor.objects.filter(estado='activo')
    #alumnos = Alumno.objects.filter(estado='activo')
    # generar el formulario
    status = "inicial"
    if request.method == 'GET':
        form = FormularioContacto()
    else:
        form = FormularioContacto(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_Email']
            message = form.cleaned_data['message']
            status = "correcto"
            try:
                mensaje = "Orla Virtual\nDE: " + name + " (" + from_email + ")\n" + message
                send_mail(subject,mensaje,['jackson1reyes2@hotmail.com'],['jackson1reyes2@gmail.com'],fail_silently=False,)
                form = FormularioContacto() # reiciniar el formulario
            except BadHeaderError:
                status = "incorrecto"

    orlas = Orla.objects.filter(codigo=id_orla)     # orla en forma de lista
    if orlas:
        orlaObject = Orla.objects.get(codigo=id_orla)   # orla como objeto
        alumnos = Alumno.objects.filter(curso=orlaObject.curso)
        profesores = Profesor.objects.filter(curso=orlaObject.curso)
        print(orlaObject)
        return render(request, 'orla.html', {'profesores': profesores,'alumnos': alumnos,'orla':orlaObject,'form':form,'status':status})
    else:
        return render(request, 'crearOrla.html')
    #if orlas.count() > 0:
    #return render(request, 'orla.html', {'curso': curso, 'profesores': profesores2,'alumnos': alumnos2,'orlas':orlas})
    #else: 
     #   return render(request, 'crearOrla.html')
    
def home(request):
    return redirect('orla/1')

"""
# Create your views here.
def contactView(request):
    if request.method == 'GET':
        form = FormularioContacto()
    else:
        form = FormularioContacto(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_Email']
            message = form.cleaned_data['message']
            try:
                mensaje = "Orla Virtual\nDE: " + name + " (" + from_email + ")\n" + message
                send_mail(subject,mensaje,['jackson1reyes2@hotmail.com'],['jackson1reyes2@gmail.com'],fail_silently=False,)
                form = FormularioContacto() # reiciniar el formulario
            except BadHeaderError:
                return render(request,'orla.html',{'form':form,'status':"incorrecto"})
            return render(request,'orla.html',{'form':form,'status':"correcto"})
    return render(request,'orla.html',{'form':form})

"""    