import csv
from collections import defaultdict
import simplekml

def readcsv(csvfile):
    with open(csvfile, 'rb') as csvfile:
        ret = csv.reader(csvfile, delimiter=';')
        r = [a for a in ret]
    return r

salarios=defaultdict(lambda: "-")
casamentos=defaultdict(lambda: "-")
matriculas=defaultdict(lambda: "-")
coordenadas=defaultdict(lambda: {"lat":0.0, "long": 0.0})

for s in readcsv("salarios.csv"):
    k = s[2]
    nk = k.decode('utf-8').lower().encode('utf-8')
    salarios[nk]=s[3]

for c in readcsv("casamentos.csv"):
    k=c[2]
    nk = k.decode('utf-8').lower().encode('utf-8')
    casamentos[nk]=c[3]

for m in readcsv("matriculas.csv"):
    k=m[2]
    nk = k.decode('utf-8').lower().encode('utf-8')
    matriculas[nk]=m[6]

for m in readcsv("coordenadas_municipios_sp.csv"):
    k=m[0]
    nk = k.decode('utf-8').lower().encode('utf-8')
    if len(m) > 4:
        lat = (float(m[3]) + float(m[1]))/2.0
        long = (float(m[4]) + float(m[2]))/2.0
        coordenadas[nk]={"lat": lat, "long": long}

#for k in coordenadas:
#    if k not in salarios.keys():
#        print "%s nao bate" % k

#for k in salarios:
#    if k not in coordenadas.keys():
#        print "%s nao bate (salarios)" % k


print """
<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
  <Document>
      <name>Dados dos Municipios de SP</name>
          <open>1</open>
          <description>Dados de salario medio, nascimentos e matriculas escolares do IBGE para municipios de SP</description>
          <Folder>
                <name>Municipios</name>
"""

for municipio in salarios.keys():
    print "\t<Placemark>"
    print "\t\t<name>%s</name>" % municipio
    print "\t\t<description>"
    print "\t\t\tsalario: %s casamentos: %s matriculas: %s" % (salarios[municipio], casamentos[municipio], matriculas[municipio])
    print "\t\t</description>"
    print "\t\t<Point>"
    print "\t\t\t<coordinates>%f,%f</coordinates>" % (coordenadas[municipio]["lat"], coordenadas[municipio]["long"])
    print "\t\t</Point>"

    print "\t</Placemark>"

print """
    </Folder>
  </Document>
</kml>

"""

