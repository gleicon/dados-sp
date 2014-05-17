import shapefile
import sys
import codecs
"""
executar com o arquivo 35MUE250GC_SIR.shx para todas as coordenadas dos municipios de SP
os outros arquivos sao regioes metropolitanas

"""



def read(file):
    sf = shapefile.Reader(file)
    sr = sf.shapeRecords()
    return sr

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "shp_to_csv <filename.dbf/shp>"
        sys.exit(-1)
    
    sr = read(sys.argv[1])
    f = codecs.open("coordenadas_municipios_sp.csv", "wb+", encoding="utf-8")
    for rr in sr:
        f.write("%s;%s;%s\n" % (rr.record[2].decode('latin-1'), rr.shape.bbox[0], rr.shape.bbox[1]))

    f.close()

