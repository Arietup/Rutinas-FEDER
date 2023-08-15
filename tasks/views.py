from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import CreateTaskForm, EntrenadorForm
from .models import Estudiante, Entrenador
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.

#? ---------------------------------------------------------------------------------------

def home(request):
    return render(request, 'home.html')

#? -------------------------- FORMULARIO DE REGISTRO --------------------------------------

def signup(request):
    
    if request.method == 'GET':
        return render(request, 'signup.html',{
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            # register user
            try:
                user = User.objects.create_user(username=request.POST['username'],
                password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect(home)
            except IntegrityError:
                return render(request, 'signup.html',{
                    'form': UserCreationForm,
                    "error" : 'Este usuario ya existe'
                })
        return render(request, 'signup.html',{
                    'form': UserCreationForm,
                    "error" : 'Contraseñas no coinciden'
                })


#? ------------------- DATOS YA PROCESADOS DE ENTRENADORES Y ESTUDIANTES -----------------------

@login_required
def task_detalle(request, task_id): #funcion para mostrar a detalle los estudiantes
    if request.method == 'GET':
        entrenador = Entrenador.objects.get(user=request.user)
        estudiante = get_object_or_404(Estudiante, pk=task_id, entrenador=entrenador.id)
        form = CreateTaskForm(instance=estudiante)
        return render(request, 'task_detalle.html',{"estudiante":estudiante, "form":form})
    else:
        try:
            entrenador = Entrenador.objects.get(user=request.user)
            estudiante = get_object_or_404(Estudiante, pk=task_id, entrenador=entrenador.id)

            estudiante.cedula = request.POST['cedula']
            estudiante.nombres = request.POST['nombres']
            estudiante.apellidos = request.POST['apellidos']
            estudiante.correo_electronico = request.POST['correo_electronico']
            estudiante.facultad = request.POST['facultad']
            estudiante.carrera = request.POST['carrera']
            estudiante.semestre_actual = request.POST['semestre_actual']
            estudiante.edad = request.POST['edad']
            id_entrenador = request.POST['entrenador']
            estudiante.entrenador = Entrenador.objects.get(id=id_entrenador)
            
            
            tiene_lesiones_enfermedades = request.POST.get('lesiones_enfermedades', False)
            
            if tiene_lesiones_enfermedades == 'on':
                tiene_lesiones_enfermedades = True
            else:
                tiene_lesiones_enfermedades = False
            
            estudiante.lesiones_enfermedades = tiene_lesiones_enfermedades
            
            estudiante.altura = float(request.POST['altura'])
            estudiante.peso = float(request.POST['peso'])
            estudiante.meses_entrenando = int(request.POST['meses_entrenando'])
        
            #variables que requieren de procesado // variables fitness
                
            (imc, estado_fisico, nivel_fitness, recomendacion_peso, 
            recomendacion_entrenamiento) = procesado_variables_fitness(estudiante.peso,  estudiante.altura, 
                                                                            estudiante.lesiones_enfermedades,
                                                                            estudiante.meses_entrenando)
                
            estudiante.imc = imc
            estudiante.estado_fisico = estado_fisico
            estudiante.nivel_fitness = nivel_fitness
            estudiante.recomendacion_peso = recomendacion_peso
            estudiante.recomendacion_entrenamiento = recomendacion_entrenamiento
            
            estudiante.save()
            return redirect('tasks')
        
        except ValueError:
            return render(request, 'task_detalle.html',{"estudiante":estudiante, "form":form,
                                                        'error': "Error al actualizar datos"})

@login_required            
def complete_task(request, task_id): #funcion para marcar estudiantes como completados
    entrenador = Entrenador.objects.get(user=request.user)
    estudiante = get_object_or_404(Estudiante, pk=task_id, entrenador=entrenador.id)
    if request.method == 'POST':
        estudiante.fecha_completado = timezone.now()
        estudiante.save()
        return redirect('tasks')

@login_required
def delete_task(request, task_id): #funcion para eliminar estudiantes
    entrenador = Entrenador.objects.get(user=request.user)
    estudiante = get_object_or_404(Estudiante, pk=task_id, entrenador=entrenador.id)
    if request.method == 'POST':
        estudiante.delete()
        return redirect('tasks')

@login_required
def tasks_all(request): #funcion para mostrar todos los estudiantes
    estudiantes = Estudiante.objects.all()
    return render(request, 'tasks_all.html',{"estudiantes":estudiantes})

@login_required
def tasks(request): #funcion para mostrar mis estudiantes #? Cambiar orden de muestra (no pude)
    
    try:
        entrenador = Entrenador.objects.get(user=request.user)
        estudiantes = Estudiante.objects.filter(entrenador=entrenador.id ,fecha_completado__isnull=True)
        return render(request, 'tasks.html', {"estudiantes":estudiantes})
    except:
        return redirect('perfil_entrenador')

@login_required
def tasks_completed(request): #funcion para mostrar los estudiantes completados #? Cambiar orden de muestra (no pude)
    try:    
        entrenador = Entrenador.objects.get(user=request.user)
        estudiantes = Estudiante.objects.filter(entrenador=entrenador.id ,fecha_completado__isnull=False)
        return render(request, 'tasks.html', {"estudiantes":estudiantes})
    except:
        return redirect('perfil_entrenador')

@login_required
def entrenadores(request): #funcion para mostrar todos los entrenadores
    entrenadores = Entrenador.objects.all()
    return render(request, 'entrenadores.html',{"entrenadores":entrenadores})

@login_required
def perfil_entrenador(request): #funcion solo para mostrar el perfil del entrenador que le pertenece al usuario
    perfil_entrenador = Entrenador.objects.filter(user=request.user)
    return render(request, 'perfil_entrenador.html', {"entrenadores":perfil_entrenador})

@login_required
def entrenador_detalle(request, entrenador_id): #funcion para mostrar los entrenadores detalladamente
    if request.method == 'GET':
        entrenador = get_object_or_404(Entrenador, pk=entrenador_id, user=request.user)
        form= EntrenadorForm(instance=entrenador)
        return render(request, 'entrenador_detalle.html', {"entrenador":entrenador, 'form': form})
    else:
        try:
            entrenador = get_object_or_404(Entrenador, pk=entrenador_id, user=request.user)
            form = EntrenadorForm(request.POST, instance=entrenador)
            form.save()
            return redirect('entrenadores')
        except ValueError:
            return render(request, 'entrenador_detalle.html', {"entrenador":entrenador, 'form': form,
                                                               'error': "Error al actualizar datos"})
        
#? ---------------------------------------------------------------------------------------

#?---------------- FORMULARIOS DE ENTRENDARES Y CREAR ESTUDIANTES ---------------------------

@login_required
def crear_entrenador(request):
    
    if request.method == 'GET':
        return render(request, 'crear_entrenador.html',{
            'form_crear_entrenador' : EntrenadorForm
        })
    else:
        try:
            form = EntrenadorForm(request.POST)
            entrenador = form.save(commit=False)
            entrenador.user = request.user
            entrenador.save()
            return redirect('perfil_entrenador')
        except ValueError:
            return render(request, 'crear_entrenador.html',{
                'form_crear_entrenador' : EntrenadorForm,
                'error': 'Por favor ingresa datos válidos'
            })

@login_required
def crear_estudiante(request):
    
    if request.method == 'GET':
        return render(request, 'crear_estudiante.html',{
            'form_crear_estudiante' : CreateTaskForm
        })
    else:
        try:
            
            #llamar variables mediante método POST una a una            
            cedula = request.POST['cedula']
            nombres = request.POST['nombres']
            apellidos = request.POST['apellidos']
            correo_electronico = request.POST['correo_electronico']
            facultad = request.POST['facultad']
            carrera = request.POST['carrera']
            semestre_actual = request.POST['semestre_actual']
            edad = request.POST['edad']
            
            id_entrenador = request.POST['entrenador']
            entrenador= Entrenador.objects.get(id=id_entrenador)
            
            tiene_lesiones_enfermedades = request.POST.get('lesiones_enfermedades', False)
            
            if tiene_lesiones_enfermedades == 'on':
                tiene_lesiones_enfermedades = True
            else:
                tiene_lesiones_enfermedades = False
            
            lesiones_enfermedades = tiene_lesiones_enfermedades
            
            altura = float(request.POST['altura'])
            peso = float(request.POST['peso'])
            meses_entrenando = int(request.POST['meses_entrenando'])
    
            #variables que requieren de procesado // variables fitness
            
            (imc, estado_fisico, nivel_fitness, recomendacion_peso, 
             recomendacion_entrenamiento) = procesado_variables_fitness(peso,  altura, 
                                                                        lesiones_enfermedades,
                                                                        meses_entrenando)
            
            #guardar variables en base de datos
            nuevo_estudiante = Estudiante.objects.create(
                cedula=cedula, nombres=nombres, apellidos=apellidos,
                correo_electronico=correo_electronico, facultad=facultad,
                carrera=carrera, semestre_actual=semestre_actual, edad=edad,
                entrenador=entrenador, altura=altura, peso=peso,
                meses_entrenando=meses_entrenando, lesiones_enfermedades=lesiones_enfermedades,
                imc=imc, estado_fisico=estado_fisico, nivel_fitness=nivel_fitness, 
                recomendacion_peso=recomendacion_peso,
                recomendacion_entrenamiento=recomendacion_entrenamiento
            )
            
            nuevo_estudiante.user = request.user
            nuevo_estudiante.save()
            
            return redirect('tasks')
        except ValueError:
            return render(request, 'crear_estudiante.html',{
                'form_crear_estudiante' : CreateTaskForm,
                'error': 'Por favor ingresa datos válidos'
            })

#? ---------------------------------------------------------------------------------------------

#? ------------------- FUNCIONES DE VARIABLES QUE REQUIEREN PROCESADO ---------------------------

def procesado_variables_fitness(peso, altura, lesiones_enfermedades, meses_entrenando):
    imc = calcular_imc(peso, altura)
    estado_fisico = calcular_estado_fisico(imc)
    nivel_fitness = calcular_nivel_fitness(lesiones_enfermedades, meses_entrenando)
    recomendacion_peso = obtener_recomendacion_peso(imc)
    recomendacion_entrenamiento = obtener_recomendacion_entrenamiento(nivel_fitness, 
                                                                              lesiones_enfermedades)
    
    return(imc, estado_fisico, nivel_fitness, recomendacion_peso, recomendacion_entrenamiento)

def calcular_imc(peso, altura)->float:
    imc = peso / (altura * altura)
    imc = round(imc, 2)  #variable con maximo dos decimales
    return imc
    
def calcular_estado_fisico(imc)->str:
    #Evaluacion del IMC en el estado físico del estudiante
    estado_fisico:str = ''
    if(imc < 18.5):
        estado_fisico = "Desnutrido"
    elif(imc >= 18.5 and imc <= 24.99):
        estado_fisico = "Normal"
    elif(imc >= 25.0 and imc <= 29.99):
        estado_fisico = "Sobrepeso"
    elif(imc >= 30.0 and imc <= 34.99):
        estado_fisico = "Obesidad Grado 1"
    elif(imc >= 35.0 and imc <= 39.99):
        estado_fisico = "Obesidad Grado 2"
    elif(imc >= 40.0):
        estado_fisico = "Obesidad Grado 3"
    return estado_fisico

def calcular_nivel_fitness(lesiones_enfermedades, meses_entrenando)-> str:
    if lesiones_enfermedades:
        nivel_fitness = '1'
    else:
        if meses_entrenando < 12:
            nivel_fitness = '1'
        elif meses_entrenando < 24:
            nivel_fitness = '2'
        else:
            nivel_fitness = '3'
    return nivel_fitness

def obtener_recomendacion_peso(imc)->str:
    if imc < 25:
        recomendacion_peso = 'Ganar peso'
    elif imc >= 25:
        recomendacion_peso = 'Perder peso'
    return recomendacion_peso

def obtener_recomendacion_entrenamiento(nivel_fitness, lesiones_enfermedades)->str:
    if lesiones_enfermedades:
        recomendacion_entrenamiento = 'Fundamentos hipertrofia'
    else:
        if nivel_fitness == '1':
            recomendacion_entrenamiento = 'Fundamentos hipertrofia'
        else:
            recomendacion_entrenamiento = 'Hipertrofia para intermedios - avanzados'
    return recomendacion_entrenamiento          

#? ----------------------------------------------------------------------------------------------------

#? -------------------- FORMULARIOS DE INCIO DE SESION Y CIERRE DE SESION ------------------------------

@login_required
def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html',{
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST
            ['password'])
        if user is None:
            return render(request, 'signin.html',{
            'form': AuthenticationForm,
            'error': 'El usuario o la contraseña son incorrectos'
        })
        else:
            login(request, user)
            return redirect('home')