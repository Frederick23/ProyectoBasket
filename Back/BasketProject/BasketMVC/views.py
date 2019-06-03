from django.http import HttpResponse
from django.shortcuts import render
from forms import PartidoForm

from BasketMVC.models import jugador, equipo, partido
import csv

## Devuelve la página de inicio ##
def index(request):
    return render(request, 'inicio.html')

## Muestra un jugador ##
def Mostrar(request):
    return render(request, 'jugador.html', {'jugadores': jugador.objects.filter(name='nombre')})

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
        upload_partido(request)
        return render(request, 'formulario_partido.html')
    else:
        form = PartidoForm()
        return render(request, 'formulario_partido.html', {'equipos': equipo.objects.all()})


def upload_partido(request):
    rows = []
    csv_file = request.FILES["csv_file"]
    csvreader = csv.reader(csv_file)
    for row in csvreader:
        rows.append(row)

    ## Obtenemos la información del partido ##

    data_form = request.POST.dict()
    local = data_form.get("equipo_local")
    visitante = data_form.get("equipo_visit")
    id1 = equipo(nombre=local)
    id2 = equipo(nombre=visitante)

    ## Creamos y guardamos el objeto partido ##
    p = partido(
        equipo1 = id1,
        equipo2 = id2,
        fecha = row[1][5],
        localizacion = id1.sede,
        fase = data_form.get("fase"),
        cuarto1 = row[6][1] + row[7][1],
        cuarto2 = row[6][2] + row[7][2],
        cuarto3 = row[6][3] + row[7][3],
        cuarto4 = row[6][4] + row[7][4],
        tanteo_final = row[6][5] + row[7][5])
    p.save()

    ## Asociamos el listado de jugadores al partido ##


    ## Rellenamos la tabla stats-jugador ##


    ## Rellenamos la tabla stats-partido ##

    ## Actualizamos los stats acumulados del jugador ##

    ## Actualizamos los stats acumulados del partido ##
