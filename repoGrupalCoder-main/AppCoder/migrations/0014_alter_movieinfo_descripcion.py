# Generated by Django 3.2.9 on 2021-12-21 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0013_movieinfo_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movieinfo',
            name='descripcion',
            field=models.CharField(max_length=5000),
        ),
    ]
