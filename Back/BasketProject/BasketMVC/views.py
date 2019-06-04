from django.http import HttpResponse
from django.shortcuts import render
from BasketMVC.forms import PartidoForm

from BasketMVC.models import jugador, equipo, partido
import csv

## Devuelve la página de inicio ##
def index(request):
    return render(request, 'inicio.html')

## Muestra varios jugadores ##
def Mostrar(request):
    return render(request, 'jugador.html', {'jugadores': jugador.objects.all()})

## Muestra un único jugador ##
def mostrar_jugador(request):
    return render(request, 'jugadores.html', {'jugador': jugador.objects.filter(name='nombre')})

## Muestra un equipo ##
def mostrar_equipo(request):
    return render(request, 'equipo.html', {'equipos': equipo.objects.filter(name='nombre')})

## Muestra listado equipos ##
def mostrar_Equipos(request):
    return render(request, 'list_equipos.html', {'equipos': equipo.objects.all()})

## Muestra un listado de partidos ##
def mostrar_Partidos(request):
    return render(request, 'list_partidos.html', {'partidos': partido.objects.all()})

## Muestra un partido ##
def mostrar_partido(request):
    return render(request, 'partido.html', {'equipos': partido.objects.filter(id='id')})

## Agrega un partido ##
def formulario_partido(request):

    ## Obtenemos la petición y mostramos el formulario ##
    if request.method == 'POST':
        form = PartidoForm(request.POST, request.FILES)
        resultado = upload_partido(request.FILES['file'], request.POST['equipo1'], request.POST['equipo2'])
        return render(request, 'prueba.html', {'resultado': resultado})
    else:
        form = PartidoForm()
        return render(request, 'formulario_partido.html', {'form': form})


def upload_partido(file, equipo1, equipo2):

    rows = []
    fila = []
    file_data = file.read().decode("utf-8")
    lines = file_data.split("\n")
    for line in lines:
        fields = line.split(",")
        for palabra in fields:
            fila.append(palabra)
        rows.append(fila.copy())
        fila.clear()


    ## Obtenemos la información del partido ##

    local = equipo1
    visitante = equipo2

    id1 = equipo.objects.get(nombre=local)
    id2 = equipo.objects.get(nombre=visitante)

    ## Creamos y guardamos el objeto partido ##
    p = partido(
        equipo1 = id1,
        equipo2 = id2,
        fecha = rows[1][5],
        localizacion = id1.sede,
        cuarto1 = rows[6][1] + "-" + rows[7][1],
        cuarto2 = rows[6][2] + "-" + rows[7][2],
        cuarto3 = rows[6][3] + "-" + rows[7][3],
        cuarto4 = rows[6][4] + "-" + rows[7][4],
        tanteo_final = rows[6][5] + "-" + rows[7][5])
    p.save()
    return rows
    ## Asociamos el listado de jugadores al partido ##


    ## Rellenamos la tabla stats-jugador ##


    ## Rellenamos la tabla stats-partido ##

    ## Actualizamos los stats acumulados del jugador ##

    ## Actualizamos los stats acumulados del partido ##
