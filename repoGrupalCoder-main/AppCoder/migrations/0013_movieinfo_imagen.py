# Generated by Django 3.2.9 on 2021-12-20 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0012_comentarios'),
    ]

    operations = [
        migrations.AddField(
            model_name='movieinfo',
            name='imagen',
            field=models.ImageField(default='', upload_to='movies'),
            preserve_default=False,
        ),
    ]
