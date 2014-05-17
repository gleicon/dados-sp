import csv
from collections import defaultdict

def readcsv(csvfile):
    with open(csvfile, 'rb') as csvfile:
        ret = csv.reader(csvfile, delimiter=';')
        r = [a for a in ret]
    return r

salarios=defaultdict(lambda: "-")
casamentos=defaultdict(lambda: "-")
matriculas=defaultdict(lambda: "-")
coordenadas=defaultdict(lambda: "-")

for s in readcsv("salarios.csv"):
    k = s[2]
    salarios[k.lower()]=s[3]

for c in readcsv("casamentos.csv"):
    k=c[2]
    casamentos[k.lower()]=c[3]

for m in readcsv("matriculas.csv"):
    k=m[2]
    matriculas[k.lower()]=m[6]

for m in readcsv("coordenadas_municipios_sp.csv"):
    k=m[0]
    coordenadas[k.lower()]="%s,%s" % (m[1], m[2])

print "Municipio,Salario,Casamentos,Matriculas,Lat,Long"

for municipio in salarios.keys():
    print "%s,%s,%s,%s,%s"% (municipio, salarios[municipio], casamentos[municipio], matriculas[municipio], coordenadas[municipio])
