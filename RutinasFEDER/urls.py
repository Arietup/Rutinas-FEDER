"""
URL configuration for RutinasFEDER project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('tasks/', views.tasks, name='tasks'),
    path('task_completed/', views.tasks_completed, name='task_completed'),
    path('tasks/all/', views.tasks_all, name='tasks_all'),
    path('tasks/create/', views.crear_estudiante, name='crear_estudiante'),
    path('tasks/<int:task_id>/', views.task_detalle, name='task_detalle'),
    path('tasks/<int:task_id>/complete', views.complete_task, name='complete_task'),
    path('tasks/<int:task_id>/delete', views.delete_task, name='delete_task'),
    path('entrenadores/<int:entrenador_id>/', views.entrenador_detalle, name='entrenador_detalle'),
    path('entrenadores/', views.entrenadores, name='entrenadores'),
    path('entrenadores/perfil/', views.perfil_entrenador, name='perfil_entrenador'),
    path('entrenadores/create/', views.crear_entrenador, name='crear_entrenador'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    
]
