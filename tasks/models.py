from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#? Crear formulario para datos del entrenador
class Entrenador(models.Model):
    cedula = models.CharField(max_length=10)
    nombres = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=40)
    correo_electronico = models.CharField(max_length=70)
    facultad = models.CharField(max_length=70)
    carrera = models.CharField(max_length=70)
    semestre_actual = models.CharField(max_length=2)
    edad = models.CharField(max_length=2)
    
    sexos = [
        ('F', 'Femenino'),
        ('M', 'Masculino')
    ]
    sexo = models.CharField(max_length=1, choices=sexos, default='M')
    
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        
        nombre_completo = self.nombres + ' ' + self.apellidos
        return nombre_completo +' - usuario '+self.user.username +' - semestre '+self.semestre_actual



class Estudiante(models.Model):
    cedula = models.CharField(max_length=10)
    nombres = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=40)
    correo_electronico = models.CharField(max_length=50)
    facultad = models.CharField(max_length=40)
    carrera = models.CharField(max_length=40)
    semestre_actual = models.CharField(max_length=2)
    edad = models.CharField(max_length=2)
    
    sexos = [
        ('F', 'Femenino'),
        ('M', 'Masculino')
    ]
    sexo = models.CharField(max_length=1, choices=sexos, default='M')
    
    lesiones_enfermedades = models.BooleanField(default=False) 
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    fecha_completado = models.DateTimeField(null=True, blank=True)
    
    entrenador = models.ForeignKey(Entrenador, null=True, blank=True, on_delete=models.PROTECT)
    
    #datos IMC
    altura = models.FloatField(null=True)
    peso = models.FloatField(null=True)
    
    #variables que requieren procesado - variables fitness
    meses_entrenando = models.IntegerField(null=True)
    imc = models.FloatField(null=True)
    
    estado_fisico = models.CharField(max_length=15, null=True)
    niveles = [
        ('1', 'Novato'),
        ('2', 'Intermedio'),
        ('3', 'Avanzado')
    ]
    nivel_fitness = models.CharField(max_length=1, choices=niveles, default='1', null=True)
    recomendacion_peso = models.CharField(max_length=20, null=True)
    recomendacion_entrenamiento = models.CharField(max_length=45, null=True)
    objetivo_conseguido = models.BooleanField(default=False)

    def __str__(self):
        
        nombre_completo = self.nombres + ' ' + self.apellidos
        nombre_entrenador = self.entrenador.nombres + ' ' + self.entrenador.apellidos
        return (nombre_completo + ' - facultad: ' +self.facultad + ' - carrera: ' +self.facultad +
                ' - semestre: ' + self.semestre_actual + ' - entrenador: ' +nombre_entrenador)