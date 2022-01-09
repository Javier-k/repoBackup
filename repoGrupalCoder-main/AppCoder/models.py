from django.db import models
from django.forms.fields import CharField


CATEGORIA = (
    ('A', 'ACCION'),
    ('S', 'SUSPENSO'),
    ('S', 'SCIFI'),
    ('R', 'ROMANCE'),
)

IDIOMA = (
    ('ES', 'ESPAÑOL'),
    ('EN', 'INGLES'),
)

ESTADO = (
    ('AG', 'AGREGADO RECIENTE'),
    ('MO', 'MAS OBSERVADO'),
    ('MV', 'MAYOR VALORACION'),

)

class MovieInfo(models.Model):
    titulo = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=5000)
    imagen = models.ImageField(upload_to='movies')
    director = models.CharField(max_length=40)
    categoria = models.CharField(choices=CATEGORIA, max_length=1)
    idioma = models.CharField(choices=IDIOMA, max_length=2)
    estado = models.CharField(choices=ESTADO, max_length=2)
    cast = models.CharField(max_length=500)
    prodYear = models.DateField()

    def __str__(self):
        return self.titulo


SELECCION_DE_ENLACE = (
    ('D', 'Link de descarga'),
    ('M', 'Mirar pelicula'),
)

class MovieLinks(models.Model):
    #peli = models.ForeignKey(MovieInfo, related_name='movie_watch_link', on_delete=models.CASCADE)
    tipo = models.CharField(choices=SELECCION_DE_ENLACE, max_length=1)
    enlace = models.URLField()

class Comentarios(models.Model):
    nombre = models.CharField(max_length=20)
    comentario = models.CharField(max_length=500)

    def __str__(self):
        return self.nombre

