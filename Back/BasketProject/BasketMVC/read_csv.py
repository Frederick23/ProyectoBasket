import csv
import re

info_partido = []
info_puntos = []
equipo1 = []
equipo2 = []
rows = []
cont = 0
cont2 = 0
rangoA1 = 0
rangoA2 = 0
rangoB1 = 0
rangoB2 = 0

with open('prueba.csv', 'r') as f:
  reader = csv.reader(f)
  rows = list(reader)

for row in rows:
    fila = re.sub(r'\W+', '', str(row))
    #print(fila)
    if fila == "Corazonistas":
        rangoB1 = cont2
    elif fila == "CorazonistasResumendeTiros":
        rangoB2 = cont2
    elif fila == "DistrtoOlimpico":
        rangoA1 = cont2
    elif fila == "DistrtoOlimpicoResumendeTiros":
        rangoA2 = cont2
    cont2 += 1

for row in rows:
    if cont in range(0,2):
        info_partido.append(row)
    elif cont in range(4,8):
        info_puntos.append(row)
    elif cont in range(rangoA1, rangoA2):
        equipo1.append(row)
    elif cont in range(rangoB1, rangoB2):
        equipo2.append(row)
    cont += 1

for fila in equipo1:
    for celda in fila:
        if(celda == ""):
            celda = 0

##print(equipo1)

print("******************")

#for fila in equipo1:
    #print(fila)
    #for celda in fila:
        #print(celda)
    #print("-----------------")