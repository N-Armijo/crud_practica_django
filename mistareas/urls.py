"""
URL configuration for mistareas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from tareas.views import create_tarea as crear
from tareas.views import listar_tareas as listar
from tareas.views import actualizar_tarea as actualizar
from tareas.views import eliminar_tarea as eliminar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', crear,name=''),
    path('listar_tareas', listar,name='listar_tareas'),
    path('actualizar/<int:id>', actualizar,name='actualizar_tarea'),
    path('eliminar/<int:id>', eliminar,name='eliminar_tarea'),
]
