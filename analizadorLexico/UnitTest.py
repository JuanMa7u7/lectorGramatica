import sys
import os

from AnalizadorLexico import AnalizadorLexico
# agregamos la carpeta lector
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/lectorGramatica")
from lector import lector
import string

print (AnalizadorLexico)
#obtengo la ruta absoluta del archivo
l = lector(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/analizadorLexico/archivoPrograma.txt")
# Construimos el texto
texto = ""
for renglon in l.leer():
    texto += renglon[0] + "\n"
# Pasamos el texto al analizador lexico
a = AnalizadorLexico(texto)
token = a.obtenerSiguienteToken()
while(token.getPalabra() is not "$"):
    print(token)
    token = a.obtenerSiguienteToken()


