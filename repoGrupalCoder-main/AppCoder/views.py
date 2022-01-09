from django.shortcuts import render
from django.http import HttpResponse, request
from AppCoder.forms import PeliForm, LinkForm, ComentForm, Peliformulario
from AppCoder.models import MovieInfo, MovieLinks, Comentarios
# Create your views here.

def inicio(request):
    return render(request, 'AppCoder/inicio.html')

def accion(request):
    return render(request, 'AppCoder/accion.html')

def romance(request):
    return render(request, 'AppCoder/romance.html')

def scifi(request):
    return render(request, 'AppCoder/scifi.html')

def suspenso(request):
    return render(request, 'AppCoder/suspenso.html')

def estrenos(request):
    return render(request, 'AppCoder/estrenos.html')

def oblivion(request):
    return render(request, 'AppCoder/oblivion.html')

def revenant(request):
    return render(request, 'AppCoder/revenant.html')

def diehard(request):
    return render(request, 'AppCoder/diehard.html')
    
def thewalk(request):
    return render(request, 'AppCoder/thewalk.html')
  
def peliform(request):
    if request.method == "POST":
        miFormulario = PeliForm(request.POST)

        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            peliInfo = MovieInfo(
                                    titulo = info["titulo"],
                                    descripcion = info["descripcion"],
                                    categoria = info["categoria"],
                                    idioma = info["idioma"],
                                    estado = info["estado"],
                                    cast = info["cast"],
                                    prodYear = info["prodYear"],
                                )
            peliInfo.save()

            return render(request,  'AppCoder/inicio.html')
    else:
        miFormulario = PeliForm()

    return render(request, 'AppCoder/peliform.html', {"miFormulario":miFormulario})

def linkform(request):
    if request.method == "POST":
        miFormulario = LinkForm(request.POST)

        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            linkInfo = MovieLinks(
                                    #peli = info["peli"],                            
                                    tipo = info["tipo"],
                                    enlace = info["enlace"],
                                )
            linkInfo.save()

            return render(request,  'AppCoder/inicio.html')
    else:
        miFormulario = LinkForm()

    return render(request, 'AppCoder/linkform.html', {"miFormulario":miFormulario})

def comentform(request):
    if request.method == "POST":
        miFormulario = ComentForm(request.POST)

        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            comentInfo = Comentarios(                    
                                    nombre = info["nombre"],
                                    comentario = info["comentario"],
                                )
            comentInfo.save()

            return render(request,  'AppCoder/inicio.html')
    else:
        miFormulario = ComentForm()

    return render(request, 'AppCoder/comentform.html', {"miFormulario":miFormulario})


def buscarPelicula(request):
    return render(request, 'AppCoder/buscarPelicula.html')

def buscar(request):
    titulo = request.GET["titulo"]
    movies = MovieInfo.objects.filter(titulo__icontains=titulo)
    
    if titulo:
        respuesta = "La pelicula que estas buscando no se encuentra disponible" 
        return render(request, "AppCoder/resultadoBusqueda.html", {"movies":movies, "titulo":titulo, "respuesta":respuesta})

    else:
        respuesta = "No enviaste datos"
        return render(request, "AppCoder/resultadoBusqueda.html", {"respuesta":respuesta})


def leerPeli(request):
    peliculas = MovieInfo.objects.all()
    contexto = {"peliculas":peliculas}

    return render(request, "AppCoder/leerPeli.html", contexto)

def eliminarPeli(request, titulo_eliminar):
    pelicula = MovieInfo.objects.get(titulo=titulo_eliminar)
    pelicula.delete()

    pelicula = MovieInfo.objects.all()
    contexto = {"pelicula":pelicula}

    return render(request, "AppCoder/leerPeli.html", contexto)

def editarPeli(request, titulo_editar):
    pelicula = MovieInfo.objects.get(titulo=titulo_editar)

    if request.method == 'POST':
        miFormulario = Peliformulario(request.POST)

        if miFormulario.is_valid:
            info = miFormulario.cleaned_data

            pelicula.titulo = info["titulo"],
            pelicula.descripcion = info["descripcion"],
            pelicula.categoria = info["categoria"],
            pelicula.idioma = info["idioma"],
            pelicula.estado = info["estado"],
            pelicula.cast = info["cast"],
            pelicula.prodYear = info["prodYear"]

            pelicula.save()
            return render(request, 'AppCoder/inicio.html')

    else:
        miFormulario=Peliformulario(initial={
                                        "titulo":pelicula.titulo,
                                        "descripcion":pelicula.descripcion,
                                        "categoria":pelicula.categoria,
                                        "idioma":pelicula.idioma,
                                        "estado":pelicula.estado,
                                        "cast":pelicula.cast,
                                        "prodYear":pelicula.prodYear,
                                        }
                            )
    return render(request, "AppCoder/editarPeli.html", {"miFormulario":miFormulario, "titulo_editar":titulo_editar})