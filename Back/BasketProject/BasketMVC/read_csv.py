import csv
from BasketMVC.models import partido
# initializing the titles and rows list
rows = []


with open('prueba.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        rows.append(row)


p = partido()

p.fecha = rows[1][5]
p.localizacion = rows[2][5]


print(rows[1][5])
print(p)