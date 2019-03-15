class lectorGram:
    def __init__(self, path):
        self.path=path
    def leer(self):
        #Lee la gramatica
        archivo = open(self.path, 'r')
        linea = archivo.readlines()
        archivo.close()
        text = []
#        print("La gramatica ha sido leida")
        #Se almacena la gramatica en una lista
        try:
            for i in range(len(linea)):
                text.append(linea[i].rstrip().split('\n'))
            #for i in range(len(text)):
            #    print(text[i])
        except:
            print("\nError garrafal en clase: lectorGram \n :c")
        return text
   

