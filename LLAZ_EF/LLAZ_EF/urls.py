"""LLAZ_EF URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path

from LLAZ_MIAPP import views




urlpatterns = [

    path('admin/', admin.site.urls),

    path ("", views.ruta_inicio, name="inicio"),

    path ("saludo/", views.saludo, name="saludo"),

    path ("ruta_integrantes/", views.ruta_integrantes, name= "ruta_integrantes"),

    path("crear_docente/",views.crear_docente,name="crear_docente"),
    path("listar_docente/",views.listar_docente,name="listar_docente"),
    path("crear_curso/",views.crear_curso,name="crear_curso"),
    path("listar_curso/",views.listar_curso,name="listar_curso"),


]
