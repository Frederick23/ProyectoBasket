from django.http import HttpResponse
from django.shortcuts import render
from datetime import time
from BasketMVC.forms import PartidoForm
import re
import copy
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
    file_data = file.read().decode("utf-8")
    lines = file_data.split("\n")
    for line in lines:
        fields = line.split(",")
        rows.append(fields)

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
                elif (primeraA == False and segundaA == True):
                    rangoB2 = cont2
                    segundaA = False
                    contVariables += 1
            elif local in limpita:
                if (primeraB==True and segundaB == True and cont2 != 3):
                    rangoA1 = cont2
                    primeraB = False
                    contVariables += 1
                elif (primeraB == False and segundaB == True):
                    rangoA2 = cont2
                    segundaB == False
                    contVariables += 1
        if contVariables == 4:
            break
        cont2 += 1

    # Dividimos en sublistas
    longitud = len(rows)

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

    # Convertimos los campos vacios en 0
    for fila in equipoA:
        for celda in fila:
            if celda == "":
                equipoA[equipoA.index(fila)][fila.index(celda)] = "0"
    for fila in equipoB:
        for celda in fila:
            if celda == "":
                equipoB[equipoB.index(fila)][fila.index(celda)] = "0"



    ## Filas "Sin Asignar"
    lugar = len(equipoA) - 3
    N_asignarA = []
    tamano = len(equipoA[lugar])
    for i in range(1, tamano):
        N_asignarA.append(equipoA[lugar][i])

    lugar2 = len(equipoB) - 3
    N_asignarB = []
    tamano2 = len(equipoB[lugar2])
    for j in range(1, tamano2):
        N_asignarB.append(equipoB[lugar2][j])


    # Creamos un diccionario con dorsal-jugador y una lista con nombre jugador + stats
    for fila in range(1, len(equipoA) - 2):
        ## Obtenemos el dorsal ##
        Dorsal = re.sub(r'[^\d]', '', equipoA[fila][0])
        ## Guardamos en la lista player sus stats ##
        for celda in range(1, 18):
            player.append(equipoA[fila][celda])
        ## Asignamos el diccionario dorsal-stats del jugador ##
        list_jugadores_stats_LOCAL[Dorsal] = player.copy()
        player.clear()
        ## Añadimos el jugador en la lista de jugadore del partido ##
        list_jugadores.append(jugador.objects.get(dorsal=Dorsal,equipo=id1.id))



    for fila in range(1, len(equipoB) - 2):
        ## Obtenemos el dorsal ##
        Dorsal = re.sub(r'[^\d]', '', equipoB[fila][0])
        ## Guardamos en la lista player sus stats ##
        for celda in range(1, 18):
            player.append(equipoB[fila][celda])
        ## Asignamos el diccionario dorsal-stats del jugador ##
        list_jugadores_stats_VISITANTE[Dorsal] = player.copy()
        player.clear()
        ## Añadimos el jugador en la lista de jugadore del partido ##
        list_jugadores.append(jugador.objects.get(dorsal=Dorsal, equipo=id2.id))
    
        ##return list_jugadores_stats_LOCAL.items()


    ## Creamos y guardamos el objeto partido ##

    p = partido.objects.create(
        equipo1 = id1,
        equipo2 = id2,
        fecha = info_partido[1][5],
        localizacion = id1.sede,
        fase = fase1,
        cuarto1 = info_puntos[2][1] + "-" + info_puntos[3][1],
        cuarto2 = info_puntos[2][2] + "-" + info_puntos[3][2],
        cuarto3 = info_puntos[2][3] + "-" + info_puntos[3][3],
        cuarto4 = info_puntos[2][4] + "-" + info_puntos[3][4],
        tanteo_final = info_puntos[2][5] + "-" + info_puntos[3][5],
    )
    p.save()

    ## Rellenamos la tabla stats-jugador ##
    ## Equipo Visitante ##
    for p1 in list_jugadores_stats_VISITANTE:
        entrada = stats_jugador.objects.create(
            id_jugador = jugador.objects.get(dorsal = p1, equipo = id2),
            id_partido = partido.objects.get( equipo1 = id1, equipo2= id2, fase = fase1),

            pts= list_jugadores_stats_VISITANTE[p1][0],
            TC2 = list_jugadores_stats_VISITANTE[p1][1].split("/")[0],
            I_TC2 = list_jugadores_stats_VISITANTE[p1][1].split("/")[1],
            TC3 = list_jugadores_stats_VISITANTE[p1][2].split("/")[0],
            I_TC3 = list_jugadores_stats_VISITANTE[p1][2].split("/")[1],
            TL = list_jugadores_stats_VISITANTE[p1][3].split("/")[0],
            I_TL = list_jugadores_stats_VISITANTE[p1][3].split("/")[1],
            AS = list_jugadores_stats_VISITANTE[p1][4],
            TAP = list_jugadores_stats_VISITANTE[p1][5],
            REBO = list_jugadores_stats_VISITANTE[p1][6],
            REBD = list_jugadores_stats_VISITANTE[p1][7],
            REBT = list_jugadores_stats_VISITANTE[p1][9],
            REC = list_jugadores_stats_VISITANTE[p1][10],
            DES =list_jugadores_stats_VISITANTE[p1][11],
            F = list_jugadores_stats_VISITANTE[p1][12],
            PER = list_jugadores_stats_VISITANTE[p1][13],
            FTO = list_jugadores_stats_VISITANTE[p1][14],
            EFI = float(list_jugadores_stats_VISITANTE[p1][16].replace("'","")),
            TIEMPO = list_jugadores_stats_VISITANTE[p1][15].replace("'", "")

        )
        entrada.save()

    ## Equipo Local ##
    for p2 in list_jugadores_stats_LOCAL:
        entrada = stats_jugador.objects.create(
            id_jugador = jugador.objects.get(dorsal = p2, equipo = id1),
            id_partido = partido.objects.get( equipo1 = id1, equipo2= id2, fase = fase1),

            pts= list_jugadores_stats_LOCAL[p2][0],
            TC2 = list_jugadores_stats_LOCAL[p2][1].split("/")[0],
            I_TC2 = list_jugadores_stats_LOCAL[p2][1].split("/")[1],
            TC3 = list_jugadores_stats_LOCAL[p2][2].split("/")[0],
            I_TC3 = list_jugadores_stats_LOCAL[p2][2].split("/")[1],
            TL = list_jugadores_stats_LOCAL[p2][3].split("/")[0],
            I_TL = list_jugadores_stats_LOCAL[p2][3].split("/")[1],
            AS = list_jugadores_stats_LOCAL[p2][4],
            TAP = list_jugadores_stats_LOCAL[p2][5],
            REBO = list_jugadores_stats_LOCAL[p2][6],
            REBD = list_jugadores_stats_LOCAL[p2][7],
            REBT = list_jugadores_stats_LOCAL[p2][9],
            REC = list_jugadores_stats_LOCAL[p2][10],
            DES =list_jugadores_stats_LOCAL[p2][11],
            F = list_jugadores_stats_LOCAL[p2][12],
            PER = list_jugadores_stats_LOCAL[p2][13],
            FTO = list_jugadores_stats_LOCAL[p2][14],
            EFI=float(list_jugadores_stats_LOCAL[p2][16].replace("'", "")),
            TIEMPO = list_jugadores_stats_LOCAL[p2][15].replace("'", "")

        )
        entrada.save()



    ## Rellenamos la tabla stats-equipo ##

    ## Equipo Local ##

    entrada1 = stats_equipo.objects.create(
        id_equipo = equipo.objects.get(nombre=local),
        id_partido = partido.objects.get(equipo1=id1, equipo2=id2, fase=fase1)
    )
    celda = equipoA[len(equipoA)-2]
    entrada1.pts = celda[1]
    entrada1.TC2 = celda[2].split("/")[0]
    entrada1.I_TC2 = celda[2].split("/")[1]
    entrada1.TC3 = celda[3].split("/")[0]
    entrada1.I_TC3 = celda[3].split("/")[1]
    entrada1.TL = celda[4].split("/")[0]
    entrada1.I_TL = celda[4].split("/")[0]
    entrada1.AS = celda[5]
    entrada1.TAP = celda[6]
    entrada1.REBO = celda[7]
    entrada1.REBD = celda[8]
    entrada1.REBT = celda[10]
    entrada1.REC = celda[11]
    entrada1.DES = celda[12]
    entrada1.F = celda[13]
    entrada1.PER = celda[14]
    entrada1.FTO = celda[15]
    entrada1.EFI = float(celda[17].replace("'", ""))

    campo = rows[len(rows)-7]
    entrada1.POS = campo[3]
    entrada1.P_POS = campo[4]
    entrada1.ZONA = campo[6].split("/")[0]
    entrada1.I_ZONA = campo[6].split("/")[1]
    entrada1.VENT = campo[8]
    entrada1.save()

    ## Equipo Visitante ##

    entrada2 = stats_equipo.objects.create(
        id_equipo=equipo.objects.get(nombre=visitante),
        id_partido=partido.objects.get(equipo1=id1, equipo2=id2, fase=fase1)
    )
    celda2 = equipoB[len(equipoB) - 2]
    entrada2.pts = celda2[1]
    entrada2.TC2 = celda2[2].split("/")[0]
    entrada2.I_TC2 = celda2[2].split("/")[1]
    entrada2.TC3 = celda2[3].split("/")[0]
    entrada2.I_TC3 = celda2[3].split("/")[1]
    entrada2.TL = celda2[4].split("/")[0]
    entrada2.I_TL = celda2[4].split("/")[0]
    entrada2.AS = celda2[5]
    entrada2.TAP = celda2[6]
    entrada2.REBO = celda2[7]
    entrada2.REBD = celda2[8]
    entrada2.REBT = celda2[10]
    entrada2.REC = celda2[11]
    entrada2.DES = celda2[12]
    entrada2.F = celda2[13]
    entrada2.PER = celda2[14]
    entrada2.FTO = celda2[15]
    entrada2.EFI = float(celda[17].replace("'", ""))

    campo2 = rows[len(rows) - 6]
    entrada2.POS = campo2[3]
    entrada2.P_POS = campo2[4]
    entrada2.ZONA = campo2[6].split("/")[0]
    entrada2.I_ZONA = campo2[6].split("/")[1]
    entrada2.VENT = campo2[8]
    entrada2.save()


    id_partido = partido.objects.get(equipo1=id1, equipo2=id2, fase=fase1)
    ## Llamada a función que actualiza las estadísticas globales de jugador y equipo ##
    actualizar_jugadores(local, visitante, id_partido)
    actualizar_equipos(local, visitante, id_partido)

    return "algo"

def actualizar_jugadores(equipo1, equipo2, partido):

    id_equipo1 = equipo.objects.get(nombre=equipo1)
    id_equipo2 = equipo.objects.get(nombre=equipo2)
    jugadores = jugador.objects.filter(equipo = id_equipo1)
    jugadoresV = jugador.objects.filter(equipo = id_equipo2)

    ## Equipo local ##
    for player in jugadores:
        datos_jugador = stats_jugador.objects.filter(id_jugador=player.id, id_partido=partido)
        if len(datos_jugador) == 1:
            player.partidos = player.partidos + 1
            player.pts = player.pts + datos_jugador[0].pts
            player.p_p = player.pts / player.partidos

            player.TC2 = player.TC2 + datos_jugador[0].TC2
            player.I_TC2 += datos_jugador[0].I_TC2
            if(player.I_TC2 != 0):
                player.TC2_P = int((player.TC2 / player.I_TC2)*100)

            player.TC3 += datos_jugador[0].TC3
            player.I_TC3 += datos_jugador[0].I_TC3
            if(player.I_TC3 != 0):
                player.TC3_P = int((player.TC3 / player.I_TC3)*100)

            if player.I_TC2 != 0 and player.I_TC3 != 0:
                player.TC_P = int(((player.TC2 + player.TC3 )/ (player.I_TC2 + player.I_TC3 ))*100)

            player.TL += datos_jugador[0].TL
            player.I_TL += datos_jugador[0].I_TL
            if(player.I_TL != 0):
                player.TL_P = int((player.TL / player.I_TL)*100)

            player.AS += datos_jugador[0].AS
            player.AS_p = player.AS / player.partidos
            player.TAP += datos_jugador[0].TAP
            player.TAP_p = player.TAP / player.partidos

            player.REBO += datos_jugador[0].REBO
            player.REBD += datos_jugador[0].REBD
            player.REBT += datos_jugador[0].REBT
            player.REB_p = player.REBT / player.partidos

            player.REC += datos_jugador[0].REC
            player.REC_p = player.REC / player.partidos
            player.DES += datos_jugador[0].DES
            player.F += datos_jugador[0].F
            player.PER += datos_jugador[0].PER
            player.FTO += datos_jugador[0].FTO

            player.save()

    ## Equipo Visitante ##
    for player2 in jugadoresV:
        datos_jugadorV = stats_jugador.objects.filter(id_jugador=player2.id, id_partido=partido)
        if len(datos_jugadorV) == 1:
            player2.partidos = player2.partidos + 1
            player2.pts = player2.pts + datos_jugadorV[0].pts
            player2.p_p = player2.pts / player2.partidos

            player2.TC2 = player2.TC2 + datos_jugadorV[0].TC2
            player2.I_TC2 += datos_jugadorV[0].I_TC2
            if(player2.I_TC2 != 0):
                player2.TC2_P = int((player2.TC2 / player2.I_TC2) * 100)

            player2.TC3 += datos_jugadorV[0].TC3
            player2.I_TC3 += datos_jugadorV[0].I_TC3
            if(player2.I_TC3 != 0):
                player2.TC3_P = int((player2.TC3 / player2.I_TC3) * 100)

            if player2.I_TC2 != 0 and player2.I_TC3 != 0:
                player2.TC_P = int(((player2.TC2 + player2.TC3) / (player2.I_TC2 + player2.I_TC3)) * 100)


            player2.TL += datos_jugadorV[0].TL
            player2.I_TL += datos_jugadorV[0].I_TL
            if(player2.I_TL != 0):
                player2.TL_P = int((player2.TL / player2.I_TL) * 100)

            player2.AS += datos_jugadorV[0].AS
            player2.AS_p = player2.AS / player2.partidos
            player2.TAP += datos_jugadorV[0].TAP
            player2.TAP_p = player2.TAP / player2.partidos

            player2.REBO += datos_jugadorV[0].REBO
            player2.REBD += datos_jugadorV[0].REBD
            player2.REBT += datos_jugadorV[0].REBT
            player2.REB_p = player2.REBT / player2.partidos

            player2.REC += datos_jugadorV[0].REC
            player2.REC_p = player2.REC / player2.partidos
            player2.DES += datos_jugadorV[0].DES
            player2.F += datos_jugadorV[0].F
            player2.PER += datos_jugadorV[0].PER
            player2.FTO += datos_jugadorV[0].FTO

            player2.save()


def actualizar_equipos(equipo1,equipo2,partido):
    id_equipo1 = equipo.objects.get(nombre=equipo1)
    id_equipo2 = equipo.objects.get(nombre=equipo2)

    datos_equipo1 = stats_equipo.objects.get(id_equipo = id_equipo1, id_partido=partido)
    datos_equipo2 = stats_equipo.objects.get(id_equipo = id_equipo2, id_partido=partido)

    ## Equipo Local ##
    id_equipo1.TC2 += datos_equipo1.TC2
    id_equipo1.I_TC2 += datos_equipo1.I_TC2

    if (id_equipo1.I_TC2 != 0):
        id_equipo1.TC2_P = int((id_equipo1.TC2 / id_equipo1.I_TC2) * 100)

    id_equipo1.TC3 += datos_equipo1.TC3
    id_equipo1.I_TC3 += datos_equipo1.I_TC3

    if (id_equipo1.I_TC3 != 0):
        id_equipo1.TC3_P = int((id_equipo1.TC3 / id_equipo1.I_TC3) * 100)

    if id_equipo1.I_TC2 != 0 and id_equipo1.I_TC3 != 0:
        id_equipo1.TC_P = int(((id_equipo1.TC2 + id_equipo1.TC3) / (id_equipo1.I_TC2 + id_equipo1.I_TC3)) * 100)

    id_equipo1.TL += datos_equipo1.TL
    id_equipo1.I_TL += datos_equipo1.I_TL

    if (id_equipo1.I_TL != 0):
        id_equipo1.TL_P = int((id_equipo1.TL / id_equipo1.I_TL) * 100)

    id_equipo1.AS += datos_equipo1.AS
    id_equipo1.TAP += datos_equipo1.TAP
    id_equipo1.REBO += datos_equipo1.REBO
    id_equipo1.REBD += datos_equipo1.REBD
    id_equipo1.REBT += datos_equipo1.REBT
    id_equipo1.REC += datos_equipo1.REC
    id_equipo1.DES += datos_equipo1.DES
    id_equipo1.F += datos_equipo1.F
    id_equipo1.PER += datos_equipo1.PER
    id_equipo1.FTO += datos_equipo1.FTO

    id_equipo1.save()

    ## Equipo Visitante ##
    id_equipo2.TC2 += datos_equipo2.TC2
    id_equipo2.I_TC2 += datos_equipo2.I_TC2

    if (id_equipo2.I_TC2 != 0):
        id_equipo2.TC2_P = int((id_equipo2.TC2 / id_equipo2.I_TC2) * 100)

    id_equipo2.TC3 += datos_equipo2.TC3
    id_equipo2.I_TC3 += datos_equipo2.I_TC3

    if (id_equipo2.I_TC3 != 0):
        id_equipo2.TC3_P = int((id_equipo2.TC3 / id_equipo2.I_TC3) * 100)

    if id_equipo2.I_TC2 != 0 and id_equipo2.I_TC3 != 0:
        id_equipo2.TC_P = int(((id_equipo2.TC2 + id_equipo2.TC3) / (id_equipo2.I_TC2 + id_equipo2.I_TC3)) * 100)

    id_equipo2.TL += datos_equipo2.TL
    id_equipo2.I_TL += datos_equipo2.I_TL

    if (id_equipo2.I_TL != 0):
        id_equipo2.TL_P = int((id_equipo2.TL / id_equipo2.I_TL) * 100)

    id_equipo2.AS += datos_equipo2.AS
    id_equipo2.TAP += datos_equipo2.TAP
    id_equipo2.REBO += datos_equipo2.REBO
    id_equipo2.REBD += datos_equipo2.REBD
    id_equipo2.REBT += datos_equipo2.REBT
    id_equipo2.REC += datos_equipo2.REC
    id_equipo2.DES += datos_equipo2.DES
    id_equipo2.F += datos_equipo2.F
    id_equipo2.PER += datos_equipo2.PER
    id_equipo2.FTO += datos_equipo2.FTO

    id_equipo2.save()
