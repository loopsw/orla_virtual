#Importamos tablas, zona horaria y panel user

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from django.utils.html import format_html # para mostrar miniatura

class Profesor(models.Model):
    ESTADOS_PROFESOR = (         #definimos los estados
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'), )
    #codigo_curso = models.ForeignKey(Curso, on_delete=models.CASCADE) 
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=150)
    profesion = models.CharField(max_length=150)
    descripcion = models.TextField()
    imagen = models.ImageField(null = True, upload_to='profesores/img')
    video = models.FileField(null = True, upload_to='profesores/video')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    estado = models.CharField(max_length=10,choices=ESTADOS_PROFESOR,default='activo')
    def getImage(self):
        if self.imagen:
            return format_html("<img src='{}' style='width:120px; height:100px;' >",self.imagen.url)
        else:
            return 'Sin imagen previa'
    getImage.short_description = 'Imagen previa'
    getImage.allow_tags = True

    class Meta:   #Creamos la clase metadatos
        ordering = ('apellidos',) #Ordena por fecha
    def __str__(self):  # función que devuelve el titulo
        return self.apellidos

# Modelo de alumno
class Alumno(models.Model):
    ESTADOS_ALUMNO = (         #definimos los estados
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'), )
    #codigo_curso = models.ForeignKey(Curso, on_delete=models.CASCADE) 
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=150)
    descripcion = models.TextField()
    imagen = models.ImageField(null = True, upload_to='alumnos/img')
    video = models.FileField(null = True, upload_to='alumnos/video')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    estado = models.CharField(max_length=10,choices=ESTADOS_ALUMNO,default='activo')

    def getImage(self):
        if self.imagen:
            return format_html("<img src='{}' style='width:120px; height:100px;' >",self.imagen.url)
        else:
            return 'Sin imagen previa'
    getImage.short_description = 'Imagen previa'
    getImage.allow_tags = True

    class Meta:   #Creamos la clase metadatos
        ordering = ('apellidos',) #Ordena por fecha
    def __str__(self):  # función que devuelve el titulo
        return self.nombre +" " + self.apellidos
        

# Modelo de los cursos
class Curso(models.Model):
    ESTADOS_CURSO = (         #definimos los estados
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'), )
    codigo = models.IntegerField(null = False, unique = True)
    titulo = models.CharField(max_length=150)
    subtitulo = models.CharField(max_length=150)
    fecha_inicio = models.DateTimeField(auto_now=False)
    fecha_fin = models.DateTimeField(auto_now=False)
    num_horas = models.IntegerField(null = False)
    logo = models.ImageField(null = True, upload_to='cursos/img')
    profesores = models.ManyToManyField(Profesor)
    alumnos = models.ManyToManyField(Alumno)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    estado = models.CharField(max_length=10,choices=ESTADOS_CURSO,default='activo')

    def getImage(self):
        if self.logo:
            return format_html("<img src='{}' style='width:120px; height:100px;' >",self.logo.url)
        else:
            return 'Sin imagen previa'
    getImage.short_description = 'Imagen previa'
    getImage.allow_tags = True

    class Meta:   #Creamos la clase metadatos
        ordering = ('titulo',) #Ordena por fecha
    def __str__(self):  # función que devuelve el titulo
        return self.titulo
    
# Modelo de los orla
class Orla(models.Model):
    ESTADOS_ORLA = (         #definimos los estados
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'), )
    codigo = models.IntegerField(null = False, unique = True)
    #id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=150)
    modelo = models.ImageField(null = True, upload_to='orla/modelos')
    curso = models.ForeignKey(Curso,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    estado = models.CharField(max_length=10,choices=ESTADOS_ORLA,default='activo')
    def getImage(self):
        if self.modelo:
            return format_html("<img src='{}' style='width:120px; height:100px;' >",self.modelo.url)
        else:
            return 'Sin imagen previa'
    getImage.short_description = 'Imagen previa'
    getImage.allow_tags = True

    class Meta:   #Creamos la clase metadatos
        ordering = ('titulo',) #Ordena por fecha
    def __str__(self):  # función que devuelve el titulo
        return self.titulo + "("+str(self.curso)+")"