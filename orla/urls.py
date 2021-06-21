from django.urls import path, include
from orla import views

urlpatterns = [
    path('', views.home, name='home'),
    path('orla/<int:id_orla>', views.orla_list, name='orla')     
]