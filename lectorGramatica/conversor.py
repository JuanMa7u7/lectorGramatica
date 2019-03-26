class conversorGram:

    def __init__(self, text):
        try:
            self.text=text
            self.obtenerConjuntoDerivaciones()
            self.obtenerSimbolosNoTerminales()
            self.obtenerSimbolosTerminales()
            self.obternerSimboloInicial()
        except Exception as ex:
            print("\nError en uno de los metodos, Clase: conversorGram")
            print(str(ex)+'\n')
    
    def obtenerConjuntoDerivaciones(self):
        try:
            self.deriv = self.text
            derivaciones = open("lectorGramatica/derivaciones.txt", "r")
            lineasDerivaciones = derivaciones.readlines()
            derivaciones.close()
            derivaciones = open("lectorGramatica/derivaciones.txt","w")
            for linea in lineasDerivaciones:
                if linea != "":
                    derivaciones.write("")
                else:
                    derivaciones.close()
            print(f"Num. de derivaciones:{len(self.deriv)}\n")
            #Escribe solo las derivaciones en derivaciones.txt
            derivaciones = open("lectorGramatica/derivaciones.txt","a+")
            for i in self.deriv:
                i_1 = str(i).lstrip("['")
                i_2 = str(i_1).rstrip(";']")
                derivaciones.write(str(i_2) + '\n')
            derivaciones.close()
            print("Derivaciones escritas en: derivaciones.txt\n")
        except Exception as ex:
            print("Error garrafal en clase: conversorGram.obtenerConjuntoDerivaciones()")
            print(str(ex)+'\n')

    def obtenerSimbolosNoTerminales(self):
        try:
            #Escribe solo los simbolos No Terminales en SimNoTerminales.txt
            noTerminales = open("lectorGramatica/SimNoTerminales.txt","r")
            lineasNoTerminales = noTerminales.readlines()
            noTerminales.close()
            noTerminales = open("lectorGramatica/SimNoTerminales.txt","w")
            
            for linea in lineasNoTerminales:
                if linea != "":
                    noTerminales.write("")
                else:
                    noTerminales.close()
            
            derivaciones = open("lectorGramatica/derivaciones.txt","r")
            lineasDerivaciones2 = derivaciones.readlines()
            derivaciones.close()
            for line in lineasDerivaciones2:
                line_1 = str(line).find("->")
                noTerminales.write(line[:line_1] + '\n')
            noTerminales.close()
            #Quita No Terminales repetidos del archivo SimNoTerminales.txt
            noTerminales = open("lectorGramatica/SimNoTerminales.txt","r")
            lineasNoTerminales2 = noTerminales.readlines()
            noTerminales.close()
            noTerminales = open("lectorGramatica/SimNoTerminales.txt","w")
            for linea in lineasNoTerminales:
                if linea != "":
                    noTerminales.write("")
            lineasNoTerminales3 = []
            for line in lineasNoTerminales2:
                if line not in lineasNoTerminales3:
                    lineasNoTerminales3.append(line)
            for line in lineasNoTerminales3:
                noTerminales.write(line)
            noTerminales.close()

            print("No Terminales escritos en: SimNoTerminales.txt\n")
        except Exception as ex:
            print("Error garrafal en clase: conversorGram.obtenerSimbolosNoTerminales()")
            print(str(ex)+'\n')

    def obtenerSimbolosTerminales(self):
        try:
            ladoDerecho = open("lectorGramatica/ladoDerecho.txt","r")
            lineasLadoDerecho = ladoDerecho.readlines()
            ladoDerecho.close()
            ladoDerecho = open("lectorGramatica/ladoDerecho.txt","w")

            for linea in lineasLadoDerecho:
                if linea != "":
                    ladoDerecho.write("")
                else:
                    ladoDerecho.close()

            ladoDerecho = open("lectorGramatica/ladoDerecho.txt","a+")
            #Escribe solo el lado derecho de las derivaciones en ladoDerecho.txt
            derivaciones = open("lectorGramatica/derivaciones.txt","r")
            lineasDerivaciones3 = derivaciones.readlines()
            for line in lineasDerivaciones3:
                line_3 = str(line).find("->")
                ladoDerecho.write(line[line_3+2:])
            ladoDerecho.close()
            print("Producciones escritas en: ladoDerecho.txt\n")
            ####################################################################
            simTerminales = open("lectorGramatica/SimTerminales.txt","r")
            lineasSimTerminales = simTerminales.readlines()
            simTerminales.close()
            simTerminales = open("lectorGramatica/SimTerminales.txt","w")

            for linea in lineasSimTerminales:
                if linea != "":
                    simTerminales.write("")
                else:
                    simTerminales.close()

            ladoDerecho = open("lectorGramatica/ladoDerecho.txt","r")
            lineasLadoDerecho = ladoDerecho.readlines()
            ladoDerecho.close()
            noTerminales = open("lectorGramatica/SimNoTerminales.txt","r")
            lineasNoTerminales3 = noTerminales.readlines()
            noTerminales.close()
            lineasNoTerminales4 = []
            for line in lineasNoTerminales3:
                lineasNoTerminales4.append(line[:-1])
            simTerminales = open("lectorGramatica/SimTerminales.txt","w")
            agregar = []
            
            for line in lineasLadoDerecho:
                quitarRepetidos = line.split()
                for i in quitarRepetidos:
                    if i not in lineasNoTerminales4 and i not in agregar:
                            agregar.append(str(i))
                            simTerminales.write(str(i)+'\n')
            simTerminales.close()
            
            simTerminales = open("lectorGramatica/SimTerminales.txt","r")
            lineasSimTerminales2 = simTerminales.readlines()
            simTerminales.close()


            for i in lineasSimTerminales2:
                if i in lineasNoTerminales4:
                    lineasSimTerminales2.remove(i)

            simTerminales = open("lectorGramatica/SimTerminales.txt","r")
            lineasSimTerminales = simTerminales.readlines()
            simTerminales.close()
            simTerminales = open("lectorGramatica/SimTerminales.txt","w")

            for linea in lineasSimTerminales:
                if linea != "":
                    simTerminales.write("")
                else:
                    simTerminales.close()
            simTerminales = open("lectorGramatica/SimTerminales.txt", "w")
            for line in lineasSimTerminales2:
                simTerminales.write(line)
            print("Simbolos terminales escritos en: SimTerminales.txt\n")
        except Exception as ex:
            print("Error garrafal en clase: conversorGram.obtenerSimbolosTerminales()")
            print(str(ex)+'\n')

    def obternerSimboloInicial(self):
        #Obtiene el simbolo inicial de la primera linea del archivo: SimNoTerminales.txt
        try:
            simInicial = open("lectorGramatica/simboloInicial.txt", "r")
            lineasSimInicial = simInicial.readlines()
            simInicial = open("lectorGramatica/simboloInicial.txt", "w")

            for linea in lineasSimInicial:
                    if linea != "":
                        simInicial.write("")
                    else:
                        simInicial.close()

            noTerminales = open("lectorGramatica/SimNoTerminales.txt", "r")
            lineasNoTerminales4 = noTerminales.readline()
            simInicial = open("lectorGramatica/simboloInicial.txt", "w")
            simInicial.write(lineasNoTerminales4)
            print("Simbolo inicial escrito en: simboloInicial.txt\n")
        except Exception as ex:
            print("Error garrafal en clase: conversorGram.obternerSimboloInicial()")
            print(str(ex)+'\n')



        
