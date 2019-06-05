import csv
import re


# Info básica del partido (localización
info_partido = []
# Puntos por periodo de cada equipo
info_puntos = []
jugador = []
# Nombre jugador, estadísticas
Listadjugadores = []
# Info de un equipo
equipo1 = []
# Info del otro equipo
equipo2 = []
# Diccionario "dorsal" - "nombre"
jugadores = {}


# Variables auxiliares
cont = 0
cont2 = 0
rangoA1 = 0
rangoA2 = 0
rangoB1 = 0
rangoB2 = 0


# Guardamos el fichero en una lista
with open('prueba.csv', 'r') as f:
  rows = list(csv.reader(f))

# Buscamos donde empiezan y terminan las listas de jugadores
for row in rows:
    # Borra lo no alfanumérico de los string
    fila = re.sub(r'\W+', '', str(row))
    # Sustituir por equipo1.nombre
    if fila == "Corazonistas":
        rangoB1 = cont2
    elif fila == "CorazonistasResumendeTiros":
        rangoB2 = cont2
    elif fila == "DistrtoOlimpico":
        rangoA1 = cont2
    elif fila == "DistrtoOlimpicoResumendeTiros":
        rangoA2 = cont2
    cont2 += 1

# Dividimos en sublistas
for row in rows:
    if cont in range(0, 2):
        info_partido.append(row)
    elif cont in range(4, 8):
        info_puntos.append(row)
    elif cont in range(rangoA1, rangoA2):
        equipo1.append(row)
    elif cont in range(rangoB1, rangoB2):
        equipo2.append(row)
    cont += 1

# Convertimos los campos vacios en 0
for fila in equipo1:
    for celda in fila:
        if celda == "":
            equipo1[equipo1.index(fila)][fila.index(celda)] = "0"
for fila in equipo2:
    for celda in fila:
        if celda == "":
            equipo2[equipo2.index(fila)][fila.index(celda)] = "0"

# Creamos un diccionario con dorsal-jugador y una lista con nombre jugador + stats
for fila in range(2, len(equipo1)-2):
    nombre = re.sub(r'\d+', '', equipo1[fila][0])
    dorsal = re.sub(r'[^\d]', '', equipo1[fila][0])
    jugadores[dorsal] = nombre
    jugador.append(nombre)
    for celda in range(1, 18):
        jugador.append(equipo1[fila][celda])
    Listadjugadores.append(jugador.copy())
    jugador.clear()

file = open("prueba.csv",'r')
rows = []
file_data = file.read().decode("utf-8")
lines = file_data.split("\n")
for line in lines:
    rows.append(line)
print(rows)
