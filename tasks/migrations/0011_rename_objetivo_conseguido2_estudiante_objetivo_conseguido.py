# Generated by Django 4.2.4 on 2023-08-05 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0010_remove_estudiante_objetivo_conseguido_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estudiante',
            old_name='objetivo_conseguido2',
            new_name='objetivo_conseguido',
        ),
    ]
