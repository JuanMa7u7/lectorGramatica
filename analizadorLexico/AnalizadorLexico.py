import string
from Token import Token as t
import sys
import os
# agregamos la carpeta lector
sys.path.append(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))) + "/lectorGramatica")
from lector import lector

class AnalizadorLexico():

    CASO_CERO = 0
    CASO_ENTERO = 1
    CASO_IDENTIFICADOR = 2
    CASO_SIMBOLO = 3
    CASO_OTRO = 4

    # Posicionamiento
    INDICE_ACTUAL = 0
    RENGLON_ACTUAL = 1

    def __init__(self, texto):
        self.__texto = texto
        self.__indiceActual = 0
        self.__renglonActual = 1

    @staticmethod
    def pruebaAnalizador():
        try:
            l = lector(os.path.dirname(os.path.dirname(os.path.abspath(
                __file__))) + "/analizadorLexico/archivoPrograma.txt")
            # Construimos el texto
            texto = ""
            for renglon in l.leer():
                texto += renglon + "\n"
            # Pasamos el texto al analizador lexico
            a = AnalizadorLexico(texto)
            token = a.obtenerSiguienteToken()
            while(token.getPalabra() is not "$"):
                #print(token)
                token = a.obtenerSiguienteToken()
            print("Analisis lexico completo\n")
        except Exception as ex:
            print("Error garrafal en clase: AnalizadorLexico.pruebaAnalizador()")
            print(str(ex)+'\n')
    # Metodo que obtiene los tokens

    def obtenerSiguienteToken(self):
        i = self.__indiceActual
        # iniciamos los casos por defecto en otro
        tipo = t.OTRO
        caso = self.CASO_OTRO
        self.__error = False
        # si ya no hay mas en el archivo, enviamos token de fin de archivo
        if len(self.__texto) <= i:
            return t(t.SIMBOLO, "$")
        # objetenemos el caracter de la posición actual
        simbolo = self.__texto[i]
        # si el caracter es cero
        if simbolo is "0":
            caso = self.CASO_CERO
            tipo = t.NUMERO_ENTERO
        # si el carcater es un número
        elif self.isNum(simbolo):
            caso = self.CASO_ENTERO
            tipo = t.NUMERO_ENTERO
        # si el caracter es una letra
        elif self.isAlpha(simbolo):
            caso = self.CASO_IDENTIFICADOR
            tipo = t.IDENTIFICADOR
        # si el caracter es un simbolo simple
        elif self.isSim(simbolo):
            caso = self.CASO_SIMBOLO
            tipo = t.SIMBOLO
        # obtenemos el indice del final del token con el metodo determinar Simbolo
        self.__indiceActual = self.determinarSimbolo(caso, i, self.__texto)
        # si hay un error lexico, el tipo cambia a error
        if self.__error:
            tipo = t.ERROR
        # si es otro caracter, se ignora (como espacios y saltos de linea)
        if tipo is t.OTRO:
            self.__indiceActual += 1
            # si es un salto de linea, se aumenta el renglon
            if simbolo == "\n":
                self.__renglonActual += 1
                AnalizadorLexico.RENGLON_ACTUAL = self.__renglonActual
            return self.obtenerSiguienteToken()
        # generamos el elemento token que sse va a retornar
        token = t(tipo, self.__texto[i:(self.__indiceActual + 1)])
        # aumentamos el indice actual 1, tomando en cuenta que es el caracter
        self.__indiceActual += 1
        # Cambiamos la variable a nivel de clase para obtenerla a travez del proyecto
        AnalizadorLexico.INDICE_ACTUAL = self.__indiceActual
        return token

    # metodo para seguir obteniendo el simbolo

    def determinarSimbolo(self, caso, indice, palabra):
        # si el caso es cero, se retorna el mismo indice
        if caso is self.CASO_CERO:
            return indice
        # si el caso es entero
        elif caso is self.CASO_ENTERO:
            # mientras sea un alfanumérico
            while self.isAlnum(palabra[indice]):
                # si llega a ser una letra, hay un error lexico
                if self.isAlpha(palabra[indice]):
                    self.error = True
                indice += 1
            return indice - 1
        # si el caso es un identificador
        elif caso is self.CASO_IDENTIFICADOR:
            # se lee la palabra mientras haya un alfanumérico
            while self.isAlnum(palabra[indice]):
                indice += 1
            return indice - 1
        # si el caso es un simbolo
        elif caso is self.CASO_SIMBOLO:
            # en caso de que haya un ':=' , se considera como un simbolo simple
            if palabra[indice] == ":" and palabra[indice + 1] == "=":
                return indice + 1
            # si no, solo se toma un caracter como simbolo simple
            return indice
        # si es otro, solo se regresa el indice
        else:
            return indice

    # determina si u caracter es numerico

    def isNum(self, s):
        if string.digits.find(s) is -1:
            return False
        return True

    # Determina si un caracter es una letra

    def isAlpha(self, s):
        if s is "ñ" or s is "Ñ":
            return True
        elif string.ascii_letters.find(s) is -1:
            return False
        return True

    # Determina si el caracter es numerico o una lentre

    def isAlnum(self, s):
        return self.isAlpha(s) or self.isNum(s)

    # Determina si el carater es un simbolo

    def isSim(self, s):
        if string.punctuation.find(s) is -1:
            return False
        return True


    def getIndice(self):
        return self.__indiceActual

    def getRenglon(self):
        return self.__renglonActual
