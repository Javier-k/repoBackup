# Generated by Django 3.2.9 on 2021-12-14 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=40)),
                ('descripcion', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='movies')),
                ('category', models.CharField(choices=[('A', 'ACCION'), ('S', 'SUSPENSO'), ('C', 'COMEDIA'), ('R', 'ROMANCE')], max_length=1)),
                ('idioma', models.CharField(choices=[('ES', 'ESPAÑOL'), ('EN', 'INGLES')], max_length=2)),
                ('estado', models.CharField(choices=[('AG', 'AGREGADO RECIENTE'), ('MO', 'MAS OBSERVADO'), ('MV', 'MAYOR VALORACION')], max_length=2)),
                ('prodYear', models.DateField()),
                ('viewsCount', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='Curso',
        ),
        migrations.DeleteModel(
            name='Entregable',
        ),
        migrations.DeleteModel(
            name='estudiante',
        ),
        migrations.DeleteModel(
            name='Profesor',
        ),
    ]
