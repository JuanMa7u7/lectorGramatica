class Nodo():
    
    # Constructor que recibe el nodo izquierdo, dereecho y valor
    def __init__(self, left, right, val):
        self.__left = left
        self.__right = right
        self.__value = val

    def setNodoIzquierdo(self, leftNode):
        self.__left = leftNode

    def setNodoDerecho(self, rightNode):
        self.__right = rightNode

    def setValue(self, value):
        self.__value = value

    def getNodoIzquierdo(self):
        return self.__left
    
    def getNodoDerecho(self):
        return self.__right

    def getValue(self):
        return self.__value

    def __str__(self):
        return "(" + str(self.getNodoIzquierdo()) + " " + str(self.getValue()) + " " + str(self.getNodoDerecho()) + ")"