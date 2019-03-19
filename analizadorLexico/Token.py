class Token():

    NUMERO_ENTERO = 1
    IDENTIFICADOR = 2
    SIMBOLO = 3
    OTRO = 4
    ERROR = 5

    def __init__(self, tipo, palabra):
        self.__tipo = tipo
        self.__palabra = palabra

    def tipoString(self):
        if self.__tipo is self.NUMERO_ENTERO:
            return "intLiteral"
        elif self.__tipo is self.IDENTIFICADOR:
            return "id"
        elif self.__tipo is self.SIMBOLO:
            return "Simbolo simple"
        elif self.__tipo is self.OTRO:
            return "ASCII"
        elif self.__tipo is self.ERROR:
            return "Error Lexico"
        else:
            return ""

    def getTipo(self):
        return self.__tipo
    
    def setTipo(self, tipo):
        self.__tipo = tipo

    def getPalabra(self):
        return self.__palabra

    def setPalabra(self, palabra):
        self.__palabra = palabra

    def __str__(self):
        return self.tipoString() + " : " + self.__palabra