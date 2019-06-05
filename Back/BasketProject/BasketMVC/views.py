from django.http import HttpResponse
from django.shortcuts import render
from BasketMVC.forms import PartidoForm
import re

from BasketMVC.models import jugador, equipo, partido, stats_equipo, stats_jugador
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
        resultado = upload_partido(request.FILES['file'], request.POST['equipo1'], request.POST['equipo2'], request.POST['fase'])
        return render(request, 'prueba.html', {'resultado': resultado})
    else:
        form = PartidoForm()
        return render(request, 'formulario_partido.html', {'form': form})


def upload_partido(file, equipo1, equipo2, fase1):

    ## Info básica del partido ##
    info_partido = []
    ## Tanteos del partido ##
    info_puntos = []
    ## Objeto jugador auxiliar como lista ##
    player = []
    ## Listado de jugadores del partido ##
    list_jugadores = []

    list_jugadores_stats_LOCAL = {}
    list_jugadores_stats_VISITANTE = {}

    ## Jugadores del equipo A (Local) ##
    equipoA = []

    ## Jugadores del equipo B (Visitante ##
    equipoB = []

    ## Variables auxiliares ##
    cont = 0
    cont2 = 1
    rangoA1 = 0
    rangoA2 = 0
    rangoB1 = 0
    rangoB2 = 0


    local = equipo1
    visitante = equipo2

    ## Id del equipo Local ##
    id1 = equipo.objects.get(nombre=local)

    ## Id de equipo Visitante ##
    id2 = equipo.objects.get(nombre=visitante)

    rows = []
    fila = []
    sucia = []
    file_data = file.read().decode("utf-8")
    lines = file_data.split("\n")
    for line in lines:
        fields = line.split(",")
        rows.append(fields)

    lista = []
    primeraA = True
    segundaA = True
    primeraB = True
    segundaB = True
    contVariables = 0
    # Buscamos donde empiezan y terminan las listas de jugadores
    for row in rows:
        for palabra in row:
            fililla = str(palabra).replace(r'\r', '')
            fililla = fililla.replace("'", "")
            limpita = re.sub(r'[ ^\s\d\w] & [ ^ /.]', '', fililla)
            if visitante in limpita:
                if (primeraA == True and segundaA == True and cont2 != 3):
                    rangoB1 = cont2
                    primeraA = False
                    contVariables += 1
                    lista.append(rangoB1)
                elif (primeraA == False and segundaA == True):
                    rangoB2 = cont2
                    segundaA = False
                    contVariables += 1
                    lista.append(rangoB2)
            elif local in limpita:
                if (primeraB==True and segundaB == True and cont2 != 3):
                    rangoA1 = cont2
                    primeraB = False
                    contVariables += 1
                    lista.append(rangoA1)
                elif (primeraB == False and segundaB == True):
                    rangoA2 = cont2
                    segundaB == False
                    contVariables += 1
                    lista.append(rangoA2)
        if contVariables == 4:
            break
        cont2 += 1

    # Dividimos en sublistas
    for row in rows:
        if cont in range(0, 2):
            info_partido.append(row)
        elif cont in range(4, 8):
            info_puntos.append(row)
        elif cont in range(rangoA1, rangoA2):
            equipoA.append(row)
        elif cont in range(rangoB1, rangoB2):
            equipoB.append(row)
        cont += 1

    return lista

    """"
    # Convertimos los campos vacios en 0
    for fila in equipoA:
        for celda in fila:
            if celda == "":
                equipoA[equipoA.index(fila)][fila.index(celda)] = "0"
    for fila in equipoB:
        for celda in fila:
            if celda == "":
                equipoB[equipoB.index(fila)][fila.index(celda)] = "0"

    # Creamos un diccionario con dorsal-jugador y una lista con nombre jugador + stats
    for fila in range(2, len(equipoA) - 2):
        ## Obtenemos el dorsal ##
        Dorsal = re.sub(r'[^\d]', '', equipoA[fila][0])
        ## Guardamos en la lista player sus stats ##
        for celda in range(1, 18):
            player.append(equipoA[fila][celda])
        ## Asignamos el diccionario dorsal-stats del jugador ##
        list_jugadores_stats_LOCAL[Dorsal] = player.copy()
        player.clear()
        ## Añadimos el jugador en la lista de jugadore del partido ##
        list_jugadores.append(jugador.object.get(dorsal=Dorsal,equipo=id1.id))

    for fila in range(2, len(equipoB) - 2):
        ## Obtenemos el dorsal ##
        Dorsal = re.sub(r'[^\d]', '', equipoB[fila][0])
        ## Guardamos en la lista player sus stats ##
        for celda in range(1, 18):
            player.append(equipoB[fila][celda])
        ## Asignamos el diccionario dorsal-stats del jugador ##
        list_jugadores_stats_VISITANTE[Dorsal] = player.copy()
        player.clear()
        ## Añadimos el jugador en la lista de jugadore del partido ##
        list_jugadores.append(jugador.object.get(dorsal=Dorsal, equipo=id1.id))
    
    """

    """
    ## Creamos y guardamos el objeto partido ##
    p = partido(
        equipo1 = id1,
        equipo2 = id2,
        fecha = info_partido[1][5],
        localizacion = id1.sede,
        ##fase = fase1,
        cuarto1 = info_puntos[2][1] + "-" + info_puntos[3][1],
        cuarto2 = info_puntos[2][2] + "-" + info_puntos[3][2],
        cuarto3 = info_puntos[2][3] + "-" + info_puntos[3][3],
        cuarto4 = info_puntos[2][4] + "-" + info_puntos[3][4],
        tanteo_final = info_puntos[2][5] + "-" + info_puntos[3][5],
        jugadores = list_jugadores
    )
    p.save()


    ## Rellenamos la tabla stats-jugador ##
    for p1 in list_jugadores_stats_VISITANTE:
        entrada = stats_jugador(
            id_jugador = jugador.objects.get(),
            id_partido = partido.objects.get(),

            pts= list_jugadores_stats_VISITANTE[p1][0],
            TC2 = list_jugadores_stats_VISITANTE[p1][0],
            I_TC2 = list_jugadores_stats_VISITANTE[p1][0],
            TC3 = list_jugadores_stats_VISITANTE[p1][0],
            I_TC3 = list_jugadores_stats_VISITANTE[p1][0],
            TL = list_jugadores_stats_VISITANTE[p1][0],
            I_TL = list_jugadores_stats_VISITANTE[p1][0],
            AS = list_jugadores_stats_VISITANTE[p1][0],
            TAP = list_jugadores_stats_VISITANTE[p1][0],
            REBO = list_jugadores_stats_VISITANTE[p1][0],
            REBD = list_jugadores_stats_VISITANTE[p1][0],
            REBT = list_jugadores_stats_VISITANTE[p1][0],
            REC = list_jugadores_stats_VISITANTE[p1][0],
            DES =list_jugadores_stats_VISITANTE[p1][0],
            F = list_jugadores_stats_VISITANTE[p1][0],
            PER = list_jugadores_stats_VISITANTE[p1][0],
            FTO = list_jugadores_stats_VISITANTE[p1][0],
            TIEMPO = list_jugadores_stats_VISITANTE[p1][0],
            EFI = list_jugadores_stats_VISITANTE[p1][0]

        )
        entrada.save()
        entrada.delete()

    for p2 in list_jugadores_stats_LOCAL:
        entrada = stats_jugador(
            id_jugador=jugador.objects.get(),
            id_partido=partido.objects.get(),

            pts=list_jugadores_stats_VISITANTE[p1][0],
            TC2=list_jugadores_stats_VISITANTE[p1][0],
            I_TC2=list_jugadores_stats_VISITANTE[p1][0],
            TC3=list_jugadores_stats_VISITANTE[p1][0],
            I_TC3=list_jugadores_stats_VISITANTE[p1][0],
            TL=list_jugadores_stats_VISITANTE[p1][0],
            I_TL=list_jugadores_stats_VISITANTE[p1][0],
            AS=list_jugadores_stats_VISITANTE[p1][0],
            TAP=list_jugadores_stats_VISITANTE[p1][0],
            REBO=list_jugadores_stats_VISITANTE[p1][0],
            REBD=list_jugadores_stats_VISITANTE[p1][0],
            REBT=list_jugadores_stats_VISITANTE[p1][0],
            REC=list_jugadores_stats_VISITANTE[p1][0],
            DES=list_jugadores_stats_VISITANTE[p1][0],
            F=list_jugadores_stats_VISITANTE[p1][0],
            PER=list_jugadores_stats_VISITANTE[p1][0],
            FTO=list_jugadores_stats_VISITANTE[p1][0],
            TIEMPO=list_jugadores_stats_VISITANTE[p1][0],
            EFI=list_jugadores_stats_VISITANTE[p1][0]

        )
        entrada.save()
        entrada.delete()
    
    """
    ## Rellenamos la tabla stats-partido ##

    ## Actualizamos los stats acumulados del jugador ##

    ## Actualizamos los stats acumulados del partido ##"""
