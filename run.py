import sys
import os
# agregamos la carpeta lector
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/lectorGramatica")
#Agregamos al sistema la ruta donde tenemos el analizador Lexico
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/AnalizadorLexico")
from lectorGramatica import lectorGramatica as lec
from analizadorLexico import AnalizadorLexico as analizadorLex
#Agregamos al sistema la ruta donde tenemos el Analizador Lexico
def main():
    try:
        #Leemos la gramatica y la dividimos
        lec.lectorGramatica.lectorGramatica()
        #Leemos el programa y obtenemos los tokens
        analizadorLex.AnalizadorLexico.pruebaAnalizador()
        print(input("Pulsa cualquier tecla para salir"))
    except Exception as ex:
        print("Error garrafal en: main()")
        print(str(ex)+'\n')
if __name__ == "__main__":
    main()

