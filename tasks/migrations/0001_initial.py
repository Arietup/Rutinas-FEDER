# Generated by Django 4.2.4 on 2023-08-04 06:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Entrenador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(max_length=10)),
                ('nombres', models.CharField(max_length=40)),
                ('apellidos', models.CharField(max_length=40)),
                ('correo_electronico', models.CharField(max_length=50)),
                ('facultad', models.CharField(max_length=40)),
                ('carrera', models.CharField(max_length=40)),
                ('semestre_actual', models.CharField(max_length=2)),
                ('edad', models.CharField(max_length=2)),
                ('sexo', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino')], default='F', max_length=1)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(max_length=10)),
                ('nombres', models.CharField(max_length=40)),
                ('apellidos', models.CharField(max_length=40)),
                ('correo_electronico', models.CharField(max_length=50)),
                ('facultad', models.CharField(max_length=40)),
                ('carrera', models.CharField(max_length=40)),
                ('semestre_actual', models.CharField(max_length=2)),
                ('edad', models.CharField(max_length=2)),
                ('sexo', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino')], default='F', max_length=1)),
                ('lesiones_enfermedades', models.BooleanField(default=False)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_completado', models.DateTimeField(null=True)),
                ('altura', models.FloatField()),
                ('peso', models.FloatField()),
                ('tiempo_entrenando', models.IntegerField()),
                ('imc', models.FloatField()),
                ('estado', models.CharField(max_length=15)),
                ('nivel', models.CharField(choices=[('1', 'Novato'), ('2', 'Intermedio'), ('3', 'Avanzado')], default='1', max_length=1)),
                ('recomendacion_peso', models.CharField(max_length=20)),
                ('recomendacion_entrenamiento', models.CharField(max_length=30)),
                ('entrenador', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tasks.entrenador')),
            ],
        ),
    ]