# Generated by Django 4.2.4 on 2023-08-05 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_alter_estudiante_estado_fisico_alter_estudiante_imc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='objetivo_conseguido',
            field=models.BooleanField(default=False),
        ),
    ]
