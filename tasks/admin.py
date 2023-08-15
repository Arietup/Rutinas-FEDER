from django.contrib import admin
from .models import Entrenador, Estudiante

class EntrenadorAdmin(admin.ModelAdmin):
    readonly_fields = ("fecha_creacion",)

class EstudianteAdmin(admin.ModelAdmin):
    readonly_fields = ("fecha_creacion",)

# Register your models here.
admin.site.register(Entrenador, EntrenadorAdmin)
admin.site.register(Estudiante, EstudianteAdmin)