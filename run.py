import sys
import os
# Traceback para determinar el error
import traceback
# agregamos la carpeta lector
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/lectorGramatica")
#Agregamos al sistema la ruta donde tenemos el analizador Sintactico
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/AnalizadorSintactico")
from lectorGramatica import lectorGramatica as lec
from AnalizadorSintactico import AnalizadorSintactico as analizadorSin
#from analizadorSintactico import matrizPredictiva as matrizP
#Agregamos al sistema la ruta donde tenemos el Analizador Lexico
def main():
    try:
        # Leemos la gramatica y la dividimos en archivos con las estructuras necesarias
        lec.lectorGramatica.lectorGramatica()
        # Creamos la instancoa del analizador Sintactico
        sintactico = analizadorSin()
        # Analizamos el programa sintacticamente y obtenemos errores
        errores = sintactico.comprobarSintaxis()
        print("Errores encontrados: " + str(len(errores)) + "\nErrores:" + str(errores))
        print(input("Pulsa cualquier tecla para salir"))
    except Exception as ex:
        print("Error garrafal en: main()")
        print(str(ex) + '\n')
        traceback.print_tb(err.__traceback__)
        print(input("Pulsa cualquier tecla para salir"))
if __name__ == "__main__":
    main()

