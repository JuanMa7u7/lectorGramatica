from . import lectorGram
from . import conversorGram
class lectorGramatica:
    def lectorGramatica():
        try:
            
            print("Iniciando\n")
            #Lee la gramatica y la almacena
            texto = lectorGram("Gramatica.txt")
            #Se determinan las producciones, simbolo inicial,
            #simbolos terminales y no terminales
            c = conversorGram(texto.leer())
            #El programa que se va a leer
            programa = "archivoPrograma.txt"



            #Se indica el fin del programa
            print(input("\nProceso terminado\nPulsa cualquier tecla para salir"))
        except :
            print("\nError garrafal en: main"
            +"\n:c")
            print(input("Pulsa cualquier tecla para salir"))