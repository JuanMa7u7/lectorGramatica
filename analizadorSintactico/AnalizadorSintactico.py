import sys
import os
#Agregamos al sistema la ruta donde tenemos el analizador Lexico
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/AnalizadorLexico")
# Agregamos el modulo LectorGramatica
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/lectorGramatica")
# Agregar el analizador semantico
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/analizadorSemantico")

from AnalizadorLexico import AnalizadorLexico as lex 
from Token import Token
from lector import lector
from ArbolExpresiones import ArbolExpresiones
from TablaValores import TablaValores

class AnalizadorSintactico():

    PATH_LADO_DERECHO = (os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/lectorGramatica/ladoDerecho.txt")
    PATH_SIMBOLOS_TERMINALES =  (os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/lectorGramatica/SimTerminales.txt")
    PATH_SIMBOLOS_NOTERMINALES = (os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/lectorGramatica/SimNoTerminales.txt")
    PATH_SIMBOLO_INICIAL = (os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/lectorGramatica/simboloInicial.txt")

    __simboloInicial = "programa"
    __simbolosTerminales = [
        ";",
        "if",
        "then",
        "end",
        "else",
        "repeat",
        "until",
        "id",
        ":=",
        "read",
        "write",
        "<",
        "=",
        "+",
        "-",
        "*",
        "/",
        "(",
        ")",
        "intLiteral",
        "$"
    ]
    __simbolosNoTerminales = [
        "programa",
        "secuencia_sent",
        "secuencia_sent'",
        "sentencia",
        "sent_if",
        "sent_if'",
        "sent_repeat",
        "sent_assign",
        "sent_read",
        "sent_write",
        "exp",
        "exp'",
        "op_comparacion",
        "exp_simple",
        "exp_simple'",
        "opsuma",
        "term",
        "term'",
        "opmult",
        "factor"
    ]
    __ladoDerechoGramatica = [
        "secuencia_sent",
        "sentencia secuencia_sent'",
        "; sentencia secuencia_sent'",
        " ",
        "sent_if",
        "sent_repeat",
        "sent_assign",
        "sent_read",
        "sent_write",
        "if exp then secuencia_sent sent_if'",
        "end",
        "else secuencia_sent end",
        "repeat secuencia_sent until exp",
        "id := exp",
        "read id",
        "write exp",
        "exp_simple exp'",
        "op_comparacion exp_simple",
        " ",
        "<",
        "=",
        "term exp_simple'",
        "opsuma term exp_simple'",
        "",
        "+",
        "-",
        "factor term'",
        "opmult factor term'",
        " ",
        "*",
        "/",
        "( exp )",
        "intLiteral",
        "id"
    ]

    matriz= [[0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 2, 0, 0, 0, 2, 0, 2, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [3, 0, 0, 4, 4, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
            [0, 5, 0, 0, 0, 6, 0, 7, 0, 8, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 11, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 17, 0, 0, 0, 0, 0, 0, 0, 0, 0, 17, 0, 17, 0],
            [19, 0, 19, 19, 19, 0, 19, 0, 0, 0, 0, 18, 18, 0, 0, 0, 0, 0, 19, 0, 19],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 21, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 22, 0, 0, 0, 0, 0, 0, 0, 0, 0, 22, 0, 22, 0],
            [24, 0, 24, 24, 24, 0, 24, 0, 0, 0, 0, 24, 24, 23, 23, 0, 0, 0, 24, 0, 24],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 26, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 27, 0, 0, 0, 0, 0, 0, 0, 0, 0, 27, 0, 27, 0],
            [29, 0, 29, 29, 29, 0, 29, 0, 0, 0, 0, 29, 29, 29, 29, 28, 28, 0, 29, 0, 29],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 30, 31, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 34, 0, 0, 0, 0, 0, 0, 0, 0, 0, 32, 0, 33, 0]]

    def __init__(self):
        self.errores = []
        self.lexico = lex(self.__construirTexto())
        self.pila = []
        self.__tablaValores = TablaValores()
        # Leemos el archivo lado derecho y lo asignamos
        l = lector(self.PATH_LADO_DERECHO)
        self.__ladoDerechoGramatica = l.leer()
        # Leemos el archivo simbolosTerminales y lo asignamos
        l = lector(self.PATH_SIMBOLOS_TERMINALES)
        self.__simbolosTerminales = l.leer()
        # Leemos el archivo simbolosNoTerminales y lo asignamos
        l = lector(self.PATH_SIMBOLOS_NOTERMINALES)
        self.__simbolosNoTerminales = l.leer()
        # Leemos el archivo simbolo inicial y lo asignamos
        l = lector(self.PATH_SIMBOLO_INICIAL)
        self.__simboloInicial = l.leer()[0]


    def comprobarSintaxis(self):
        self.pila.append(self.__simboloInicial)
        tokenActual = self.lexico.obtenerSiguienteToken()
        tokenCimaPilaAnt = ""
        self.__expresion = []
        # auxiliar para manejar la asignación
        self.__asign = ""
        # auxiliar para el tipo de la expresion
        self.__tipoExp = ""
        #mientras la pila no este vacia
        while self.pila:
            # print(trazador)
            # Se designan los simbolos no terminales a trazar
            # self.trazarSimboloNoTerminal(self.pila[-1], "exp", self.obtenerExpresión, self.evaluarExpresion)
            self.trazarSimboloNoTerminal(self.pila[-1], "sent_assign", self.agregarAsignacion, self.asignarExpresion, tokenAct=tokenActual)
            
            # Obtiene el ultimo elemento
            tokenCimaPila = self.pila[-1]
            valor = 0
            # Comprueba si es un error lexico
            if tokenActual.getTipo() is Token.ERROR:
                self.errores.append("error Lexico, el token : " + tokenActual.getPalabra() + " no es aceptado")
                tokenActual = self.lexico.obtenerSiguienteToken()
            elif tokenCimaPila in self.__simbolosNoTerminales:
                #si el token actual es la cima de la pila, lo buscamos
                if tokenActual.getPalabra() in self.__simbolosTerminales:
                    valor = self.matriz[self.__simbolosNoTerminales.index(tokenCimaPila)][self.__simbolosTerminales.index(tokenActual.getPalabra())]
                # si no, si el tipo de el token esta en la cima pila, lo buscamos
                elif tokenActual.tipoString() in self.__simbolosTerminales:
                    valor = self.matriz[self.__simbolosNoTerminales.index(tokenCimaPila)][self.__simbolosTerminales.index(tokenActual.tipoString())]
                #si el valor obtenido no es 0
                if valor is not 0:
                    self.pila.pop()
                    aux = self.__ladoDerechoGramatica[(valor - 1)]
                    palabrasDerivadas = aux.split(" ")
                    for i in range(len(palabrasDerivadas) - 1, -1, -1):
                        self.pila.append(palabrasDerivadas[i])
                #si no, se agrega alos errores
                else:
                    self.errores.append("error Sintaxis, se esperaba: " + tokenCimaPila + " y se encontro " + tokenActual.getPalabra() + " en la linea: " + str(self.lexico.getRenglon()))
                    tokenActual = self.lexico.obtenerSiguienteToken()
            #si es un terminal
            elif tokenCimaPila in self.__simbolosTerminales:
                #comparamos si es el mismo
                if (tokenCimaPila == tokenActual.getPalabra()) or (tokenCimaPila == tokenActual.tipoString()):
                    self.pila.pop()
                    tokenActual = self.lexico.obtenerSiguienteToken()
                # si no, es un error
                else:
                    self.errores.append("error Sintaxis, se esperaba: " + tokenCimaPila + " y se encontro " + tokenActual.getPalabra() + " en la linea: " + str(self.lexico.getRenglon()))
                    tokenActual = self.lexico.obtenerSiguienteToken()
            # si se agrego una produccion que deriva a vacio, se quita
            elif not tokenCimaPila:
                self.pila.pop()
            #si se encontro el fin de archivo, regresamos la lista de errorres
            if tokenActual.getPalabra() == "$" and tokenCimaPila == tokenCimaPilaAnt :
                return self.errores
            # se asigna el token anterior para comprobar que no se cicle y termina correctamente
            tokenCimaPilaAnt = tokenCimaPila
        
        print(self.__tablaValores.getTablaValores())
        return self.errores


    # Función Auxiliar para la construcciopn del texto
    def __construirTexto(self):
        #obtengo la ruta absoluta del archivo
        l = lector(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/analizadorLexico/archivoPrograma.txt")
        # Construimos el texto
        texto = ""
        for renglon in l.leer():
            texto += renglon + "\n"
        return texto

    # Función para dar trazabilidad a un simbolo no terminal
    def trazarSimboloNoTerminal(self, tokenCimaPila, tokenATrazar, funcTrazado, funcFinal, **kwargs):
        # Si el token trazado es el token actual, lo sacamos
        if ("#" + tokenATrazar) == self.pila[-1]:
            self.pila.pop()
            funcFinal()
        # si la lista no contiene el token trazado y es igual al token actual
        elif not ("#" + tokenATrazar) in self.pila and tokenCimaPila == tokenATrazar:
            # Inserto un token de seguimiento con el simbolo '#' (hashtag) para identificarlo 
            self.pila.insert(-1, "#" + tokenATrazar)
        # si el token trazado esta en la pila, se ejecuta la funcion
        if ("#" + tokenATrazar) in self.pila:
            # Se ejecuta la función del trazado enviandole los elementos de la pila del trazado
            if not kwargs:
                funcTrazado(self.pila[self.pila.index("#" + tokenATrazar):])
            else:
                funcTrazado(self.pila[self.pila.index("#" + tokenATrazar):], **kwargs)


    # función para incluir los simbolos de la expresión en una lista
    def obtenerExpresión(self, pila, **kwargs):
        ultimoElemento = pila[-1]
        if ultimoElemento in self.__simbolosTerminales:
            if ultimoElemento == 'id':
                # Aumentamos el conteo del identificador
                self.__tablaValores.aumentarRepeticionTokenPorNombre(kwargs["tokenAct"].getPalabra())
                ultimoElemento = self.__tablaValores.buscarToken(kwargs["tokenAct"].getPalabra())[2]
            self.__expresion.append(ultimoElemento)
            print("Elementos Recibidos en Expresion " + str(pila))

    # función que construye el arbol a partir de la expressión
    def evaluarExpresion(self):
        print(self.__expresion)
        a = ArbolExpresiones(self.__expresion, ["+","-","*","/","<",">","="])
        self.__tipoExp = a.evaluar()
        errores = a.getErrores()
        # Se agregan los errores encontrados
        if errores:
            self.errores.append(errores)
        # Reset expresión
        self.__expresion = []
        print("Resultado evaluado: " + str(self.__tipoExp))

    # función para obtener la asiganción de la expresión
    def agregarAsignacion(self, pila, **kwargs):
        # Obtenemos el simbolo de asignación
        if not self.__asign and pila[-1] not in self.__simbolosNoTerminales:
            self.__asign = kwargs["tokenAct"].getPalabra()
            print()
        # TODO: obtener el simbolo genericamente, no harcodeado
        elif not pila[-1] == ":=":
            self.trazarSimboloNoTerminal(self.pila[-1], "exp", self.obtenerExpresión, self.evaluarExpresion, **kwargs)

    # funcion para asignar al final de el trazado de asignación
    def asignarExpresion(self):
        self.__tablaValores.agregarToken(self.__asign, self.__tipoExp )
        # Reiniciamos a valores vacios
        self.__asign = ""
        self.__tipoExp = ""





    

