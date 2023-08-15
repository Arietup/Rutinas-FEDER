from django import forms
from .models import Estudiante, Entrenador


class EntrenadorForm(forms.ModelForm):
    class Meta:
        model = Entrenador
        fields = ['cedula', 'nombres', 'apellidos', 'correo_electronico',
                  'facultad', 'carrera', 'semestre_actual', 'edad',
                  'sexo']
        widgets = {
            'cedula': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe tu numero de cedula'}),
            'nombres': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe tus dos nombres'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe tus dos apellidos'}),
            'correo_electronico': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe tu correo electronico'}),
            'facultad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe el nombre de tu facultad'}),
            'carrera': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe el nombre de tu carrera'}),
            'semestre_actual': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe tu semestre actual'}),
            'edad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe tu edad'}),
        }


class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['cedula', 'nombres', 'apellidos', 'correo_electronico',
                  'facultad', 'carrera', 'semestre_actual', 'edad',
                  'sexo', 'lesiones_enfermedades', 'entrenador', 'altura',
                  'peso', 'meses_entrenando',]
        widgets = {
            'cedula': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Numero de cedula'}),
            'nombres': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe los dos nombres'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe los dos apellidos'}),
            'correo_electronico': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe el correo electronico'}),
            'facultad': forms.TextInput(attrs={'class': 'form-control' , 'placeholder': 'Escribe el nombre de la facultad'}),
            'carrera': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe el nombre de la carrera'}),
            'semestre_actual': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe el semestre actual'}),
            'edad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe la edad'}),
            'altura': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Escribe la altura en metros'}),
            'peso': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Escribe el peso en kilogramos'}),
            'meses_entrenando': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Escribe la cantidad de meses entrenando'}),
        }