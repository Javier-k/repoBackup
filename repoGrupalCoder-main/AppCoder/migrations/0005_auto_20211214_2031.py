# Generated by Django 3.2.9 on 2021-12-14 23:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0004_alter_movieinfo_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='movieinfo',
            name='cast',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='MovieLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('D', 'Link de descarga'), ('M', 'Mirar pelicula')], max_length=1)),
                ('enlace', models.URLField()),
                ('peli', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_watch_link', to='AppCoder.movieinfo')),
            ],
        ),
    ]
