# Generated by Django 2.1.15 on 2021-06-21 04:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especialidad', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=11)),
                ('nombreM', models.CharField(max_length=80)),
                ('apaterno', models.CharField(max_length=80)),
                ('especialidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Especialidad')),
            ],
        ),
        migrations.CreateModel(
            name='reserva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=11)),
                ('nombre', models.CharField(max_length=80)),
                ('apaterno', models.CharField(max_length=80)),
                ('amaterno', models.CharField(max_length=80)),
                ('correo', models.EmailField(max_length=200)),
                ('fecha_nacimiento', models.CharField(max_length=80)),
                ('sexo', models.CharField(max_length=20)),
                ('fecha_reservaR', models.CharField(max_length=80)),
                ('montoR', models.FloatField()),
                ('horaR', models.CharField(max_length=80)),
                ('especialidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Especialidad')),
                ('nombreM', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Medico')),
            ],
        ),
    ]
