from django import forms
from django.forms import Form
from AppCoder.models import MovieInfo, CATEGORIA, IDIOMA, ESTADO, SELECCION_DE_ENLACE

class PeliForm(forms.Form):
    titulo = forms.CharField()
    descripcion = forms.CharField()
    imagen = forms.ImageField()
    director = forms.CharField()
    categoria = forms.ChoiceField(choices=CATEGORIA)
    idioma = forms.ChoiceField(choices=IDIOMA)
    estado = forms.ChoiceField(choices=ESTADO)
    cast = forms.CharField()
    prodYear = forms.DateField()

    def __str__(self):
        return self.titulo

class LinkForm(forms.Form):
    
    #peli = forms.ChoiceField()
    tipo = forms.ChoiceField(choices=SELECCION_DE_ENLACE)
    enlace = forms.URLField()
    
    def __str__(self):
        return self.peli


class ComentForm(forms.Form):
    nombre = forms.CharField()
    comentario = forms.CharField()

class Peliformulario(forms.Form):
    titulo = forms.CharField()
    descripcion = forms.CharField()
    imagen = forms.ImageField()
    director = forms.CharField()
    categoria = forms.ChoiceField(choices=CATEGORIA)
    idioma = forms.ChoiceField(choices=IDIOMA)
    estado = forms.ChoiceField(choices=ESTADO)
    cast = forms.CharField()
    prodYear = forms.DateField()

    def __str__(self):
        return self.titulo