class lector:
    def __init__(self, path):
        try:
            self.path = path
        except Exception as ex:
            print("\nError en uno de los metodos, Clase: lector")
            print(str(ex)+'\n')
    def leer(self):
        #Lee la gramatica
        try:
            archivo = open(self.path, 'r')
            linea = archivo.readlines()
            archivo.close()
            text = []
        #print("La gramatica ha sido leida")
        #Se almacena la gramatica en una lista
        
            for i in range(len(linea)):
                text.append(linea[i].split('\n')[0])
            #for i in range(len(text)):
            #    print(text[i])
        except Exception as ex:
            print("\nError garrafal en: lector.leer()")
            print(str(ex)+'\n')
        return text
   

