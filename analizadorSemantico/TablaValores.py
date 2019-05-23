class TablaValores():

    TIPO_NUMBER = 0
    TIPO_BOOLEAN = 1
    TIPO_INDEFINIDO = 2

    def __init__(self):
        self.__tablaValores = [] 

    # Metodo que agrega el valor con su tipo identificado
    def agregarToken(self, token, tipo, val = None):
        tokenBuscado = self.buscarToken(token)
        if val is None:
            val = self.__defaultValue(tipo)
        if tokenBuscado is None:
            self.__tablaValores.append([self.obtenerIdToken(tokenBuscado), token, tipo, self.identificarValor(tipo), val, 1])
        else:
            self.aumentarRepeticionToken(self.obtenerIdToken(tokenBuscado))


    # Metodo que busca si el token existe en la tabla
    def buscarToken(self, token):
        for item in self.__tablaValores:
            if token == item[1]:
                return item
        return None


    # Metodo que devuelve el idToken o genera uno nuevo
    def obtenerIdToken(self, token):
        if token is None:
            if len(self.__tablaValores) > 0:
                return self.__tablaValores[-1][0] + 1
            else:
                return 1
        return token[0]


    # Metodo para aumentar el valor del token en las veces encontrado
    def aumentarRepeticionToken(self, id):
        self.__tablaValores[id - 1][5] += 1

    # Metodo para aumentar la repetición del token por su nombre
    def aumentarRepeticionTokenPorNombre(self, tokenVal):
        self.aumentarRepeticionToken(self.obtenerIdToken(self.buscarToken(tokenVal)))

    # Este metodo identifica el tipo del valor
    # Devuelve un número correspondiente al valor que identifica
    def identificarValor(self, valor):
        #si es un número
        if self.isNumeric(valor):
            return self.TIPO_NUMBER
        #si es un boolean
        elif self.isBoolean(valor):
            return self.TIPO_BOOLEAN
        #si no se determino el tipo
        else:
            return self.TIPO_INDEFINIDO
    
    #verifica si el valor es un numero
    def isNumeric(self, valor):
        if valor == "intLiteral":
            return True
        return False

    #verifica si el valor es un boolean
    def isBoolean(self, valor):
        if valor == "boolean":
            return True
        return False

    # Obtiene el valor por defecto
    def __defaultValue(self, type):
        if self.isNumeric(type):
            return 0
        elif self.isBoolean(type):
            return False
        else:
            return "Desconocido"
        
    # Get tabla
    def getTablaValores(self):
        return self.__tablaValores