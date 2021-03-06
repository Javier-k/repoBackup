# Generated by Django 3.2.9 on 2021-12-21 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0016_auto_20211220_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movieinfo',
            name='estado',
            field=models.CharField(choices=[('AG', 'AGREGADO RECIENTE'), ('MO', 'MAS OBSERVADO'), ('MV', 'MAYOR VALORACION')], max_length=2),
        ),
        migrations.AlterField(
            model_name='movieinfo',
            name='idioma',
            field=models.CharField(choices=[('ES', 'ESPAÑOL'), ('EN', 'INGLES')], max_length=2),
        ),
    ]
