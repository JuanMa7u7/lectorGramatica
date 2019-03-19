import sys
import os
# agregamos la carpeta lector
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/lectorGramatica")
#Agregamos al sistema la ruta donde tenemos el analizador Lexico
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/AnalizadorLexico")
from lectorGramatica import lectorGramatica as lec

#Agregamos al sistema la ruta donde tenemos el Analizador Lexico
def main():
    
    print("Chingas a tu madre pinche Victor")
    lec.lectorGramatica.lectorGramatica()
    #Leemos el programa y obtenemos los tokens

if __name__ == "__main__":
    main()

