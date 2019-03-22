import sys
import os
#Agregamos al sistema la ruta donde tenemos el analizador Lexico
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/AnalizadorLexico")
# Agregamos el modulo LectorGramatica
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/lectorGramatica")

from AnalizadorLexico import AnalizadorLexico as lex 
from Token import Token
from lector import lector

class AnalizadorSintactico():

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


    def comprobarSintaxis(self):
        self.pila.append(self.__simboloInicial)
        tokenActual = self.lexico.obtenerSiguienteToken()
        #mientras la pila no este vacia
        while self.pila:
            # obtiene el ultimo elemento
            tokenCimaPila = self.pila[-1]
            valor = 0
            #comprueba si es un error lexico
            if tokenActual.getTipo() is Token.ERROR:
                self.errores.append("error Lexico, el token : " + tokenActual.getPalabra() + " no es aceptado \n")
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
                    self.errores.append("error Sintaxis, se esperaba: " + tokenCimaPila + " y se encontro " + tokenActual.getPalabra() + "\n")
                    tokenActual = self.lexico.obtenerSiguienteToken()
            #si es un terminal
            else:
                #comparamos si es el mismo
                if (tokenCimaPila == tokenActual.getPalabra()) or (tokenCimaPila == tokenActual.tipoString()):
                    self.pila.pop()
                    tokenActual = self.lexico.obtenerSiguienteToken()
                    
                # si se agrego una produccion que deriva a vacio, se quita
                elif not tokenCimaPila:
                    self.pila.pop()
                # si no, es un error
                else:
                    self.errores.append("error Sintaxis, se esperaba: " + tokenCimaPila + " y se encontro " + tokenActual.getPalabra() + "\n")
                    tokenActual = self.lexico.obtenerSiguienteToken()
            #si se encontro el fin de archivo, regresamos la lista de errorres
            if tokenActual.getPalabra() == "$":
                return self.errores
        return self.errores


    # Función Auxiliar para la construcciopn del texto
    def __construirTexto(self):
        #obtengo la ruta absoluta del archivo
        l = lector(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/analizadorLexico/archivoPrograma.txt")
        # Construimos el texto
        texto = ""
        for renglon in l.leer():
            texto += renglon[0] + "\n"
        return texto

    

