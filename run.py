import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/lectorGramatica")
from lectorGramatica import lectorGramatica as lec

#Agregamos al sistema la ruta donde tenemos el Analizador Lexico
def main():
    #print(sys.path.append(os.path.dirname(
    #    os.path.abspath(__file__)) + "/lectorGramatica"))
    print("Chingas a tu madre pinche Victor")
    lec.lectorGramatica.lectorGramatica()

if __name__ == "__main__":
    main()

