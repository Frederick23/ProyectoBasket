from django.http import HttpResponse
from django.shortcuts import render
from BasketMVC.models import jugador
from BasketMVC.models import partido
import csv


def index(request):
    return HttpResponse("Hola y bienvenido al index")


def Mostrar(request):
    return render(request, 'tabla.html', {'jugadores': jugador.objects.all()})


def upload_partido(request):
    rows = []
    csv_file = request.FILES["csv_file"]
    csvreader = csv.reader(csv_file)
    for row in csvreader:
        rows.append(row)

    ## Obtenemos la información del partido ##

    ## Creamos y guardamos el objeto partido ##

    ## Asociamos el listado de jugadores al partido ##

    ## Rellenamos la tabla stats-jugador ##

    ## Rellenamos la tabla stats-partido ##

    ## Actualizamos los stats acumulados del jugador ##

    ## Actualizamos los stats acumulados del partido ##
