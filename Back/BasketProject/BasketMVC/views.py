from django.http import HttpResponse
from django.shortcuts import render

from BasketMVC.models import jugador, equipo, partido
import csv


def index(request):
    return HttpResponse("Hola y bienvenido al index")


def Mostrar(request):
    return render(request, 'tabla.html', {'jugadores': jugador.objects.all()})

def formulario_partido(request):
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
