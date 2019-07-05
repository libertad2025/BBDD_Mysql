# -*- coding: utf-8 -*-
# Generated by Django 1.11b1 on 2019-07-05 10:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('modelos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=50)),
                ('login', models.CharField(max_length=30)),
                ('pais', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('comentario', models.CharField(max_length=1000)),
                ('fecha_creacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelos.Autor')),
            ],
        ),
        migrations.RemoveField(
            model_name='matricula',
            name='Alumno',
        ),
        migrations.RemoveField(
            model_name='matricula',
            name='Curso',
        ),
        migrations.DeleteModel(
            name='Alumno',
        ),
        migrations.DeleteModel(
            name='Curso',
        ),
        migrations.DeleteModel(
            name='Matricula',
        ),
    ]
