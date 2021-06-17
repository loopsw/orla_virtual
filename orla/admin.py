from django.contrib import admin

# Register your models here.
from .models import Profesor, Alumno,Curso,Orla


#Alumno
class AlumnoAdmin(admin.ModelAdmin):
    # Campos visibles a la hora de crear Alumno
    fields = ('nombre','apellidos','descripcion','imagen','getImage','video','estado','created','updated',)
    # Campos que muestra en resumen
    list_display= ('apellidos','nombre','getImage','estado','created','updated',)
    readonly_fields = ('getImage','created','updated',)
admin.site.register(Alumno,AlumnoAdmin)

# Profesor
class ProfesorAdmin(admin.ModelAdmin):
    # Campos visibles a la hora de crear Alumno
    fields = ('nombre','apellidos','profesion','descripcion','imagen','getImage','video','estado','created','updated',)
    # Campos que muestra en resumen
    list_display= ('apellidos','nombre','getImage','profesion','estado','created','updated',)
    readonly_fields = ('getImage','created','updated',)
admin.site.register(Profesor,ProfesorAdmin)

# Curso
class CursoAdmin(admin.ModelAdmin):
    # Campos visibles a la hora de crear Alumno
    fields = ('codigo','titulo','subtitulo','fecha_inicio','fecha_fin','logo','getImage','profesores','alumnos','estado','created','updated',)
    # Campos que muestra en resumen
    list_display= ('titulo','subtitulo','fecha_inicio','fecha_fin','getImage','estado','created','updated',)
    readonly_fields = ('getImage','created','updated',)
admin.site.register(Curso,CursoAdmin)

# Curso
class OrlaAdmin(admin.ModelAdmin):
    # Campos visibles a la hora de crear Alumno
    fields = ('codigo','titulo','modelo','getImage','curso','created','updated',)
    # Campos que muestra en resumen
    list_display= ('titulo','curso','getImage','created','updated',)
    readonly_fields = ('getImage','created','updated',)
admin.site.register(Orla,OrlaAdmin)
