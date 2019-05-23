import operator
from Nodo import Nodo
from AnalizadorLexico import AnalizadorLexico
class ArbolExpresiones():

    NUMEROS = ['intLiteral']

    def __init__(self, expression, operators):
        self.__root = None
        self.__operators = operators
        self.__root = self.constructTree(expression)
        self.__errores = []

    # convierte la expresión a arbol de expresiónes
    def constructTree(self, postfix): 
        # pilas para guardar los valores y los operadores
        operands = []
        operators = []
        brincar = 0
        # Traverse through every character of input expression 
        for index,char in enumerate(postfix) : 
            if brincar != 0:
                brincar-= 1
            elif char == "(":
                subExp = postfix[index + 1:self.indiceParentesis(postfix[index + 1:]) + index + 1]
                brincar = len(subExp) + 1
                t = self.constructTree(subExp)
                operands.append(t)
            elif char == ")":
                break

            # if operand, simply push into stack 
            elif not char in self.__operators:
                t = Nodo(None, None, char)
                operands.append(t) 
    
            # Operator 
            else: 
                # Pop two top nodes 
                t = Nodo(None, None, char) 
                operators.append(t)
        # iteramos por cada operador
        # TODO: change priority on solving operations
        for i in range(len(operators)):
            op = operators.pop()
            val1 = operands.pop()
            val2 = operands.pop()
            # asignamos los nodos izquierdo y derecho al operador
            op.setNodoIzquierdo(val1)
            op.setNodoDerecho(val2)
            # lo metemos a operandos para que sea el que sigue de valor
            operands.append(op)

        # Only element  will be the root of expression tree 
        t = operands.pop()
        # print(t)
        return t

    # Obtiene el indice del parentesis al mismo nivel
    def indiceParentesis(self, exp):
        parentesis = 1
        print("expresin en parentesis " + str(exp))
        for val,el in enumerate(exp):
            if el == "(":
                parentesis += 1
            elif el == ")":
                parentesis -= 1
            if parentesis == 0:
                print("indice parentesis " + str(val))
                return val
        return -1

    # función que evalua el tipo de expresión
    def evaluar(self, node=None):
        
        if node == None:
            node = self.__root
        # si es un valor
        if not node.getValue() in self.__operators:
            return node.getValue()
        # si es un operador
        else:
            left = self.evaluar(node.getNodoIzquierdo())
            right = self.evaluar(node.getNodoDerecho())

            return self.evaluarPorSimbolo(node.getValue())(left,right)
        

    def solve(self):
        return self.__calculate(self.__root)
    

    def __calculate(self, node):
        print(self.__operators)
        print(node.getValue())

        # si el nodo esta vacio, se regresa error
        if node == None:
            raise Exception("La Expresion debe tener algun numero")
        
        # Si es un valor, se retorna el valor
        if not node.getValue() in self.__operators:
            return node.getValue()
        
        # Si es un operador
        left = self.__calculate(node.getNodoIzquierdo())
        right = self.__calculate(node.getNodoDerecho())

        print("left : " +str(left) + " right: " + str(right))
        func = node.getValue()
        if callable(func):
            return func(left, right)
        else:
            return self.operadorPorSimbolo(func)(left, right)


    # Obtiene el operador según el simbolo
    def operadorPorSimbolo(self, val):
        if val == "+":
            return operator.add
        elif val == "-":
            return operator.sub
        elif val == "*":
            return operator.mul
        elif val == "/":
            return operator.truediv
        elif val == "<":
            return operator.lt
        elif val == ">":
            return operator.gt
        elif val == "=":
            return operator.eq
        else:
            return operator.is_

    # Evaluar segun el simbolo
    def evaluarPorSimbolo(self, val):
        if val == "+":
            return self.evaluarOperacionAritmetica
        elif val == "-":
            return self.evaluarOperacionAritmetica
        elif val == "*":
            return self.evaluarOperacionAritmetica
        elif val == "/":
            return self.evaluarOperacionAritmetica
        elif val == "<":
            return self.evaluarOperacionLogicaMayorYMenorQue
        elif val == ">":
            return self.evaluarOperacionLogicaMayorYMenorQue
        elif val == "=":
            return self.evaluarOperacionLogicaIgualdad
        else:
            return self.evaluarOperacionLogicaIgualdad

    # Evaluar Operación aritmetica simbolica
    def evaluarOperacionAritmetica(self, a, b):
        # TODO: Change return by numerical order
        if a in self.NUMEROS and b in self.NUMEROS:
            return 'intLiteral'
        else:
            # raise Exception("No se pueden operar aritmeticamente los tipos: " + a + " y " + b)
            self.__errores.append("Error Semantico: No se pueden operar aritmeticamente los tipos " 
                + a + " y " + b + " en el renglon: " + str(AnalizadorLexico.RENGLON_ACTUAL))

    # Evaluar Operación logica Mayor y Menor simbolica
    def evaluarOperacionLogicaMayorYMenorQue(self, a, b):
        if a in self.NUMEROS and b in self.NUMEROS:
            return 'boolean'
        else:
            # raise Exception("No se pueden comparar mayor o menor que los tipos: " + a + " y " + b)
            self.__errores.append("No se pueden comparar mayor o menor que los tipos: " 
                + a + " y " + b + " en el renglon: " + str(AnalizadorLexico.RENGLON_ACTUAL))

    # Evaluar Operación lógica igualdad simbolica
    def evaluarOperacionLogicaIgualdad(self, a, b):
        if a in self.NUMEROS and b in self.NUMEROS:
            return 'boolean'
        elif a == 'boolean' and b == 'boolean':
            return 'boolean'
        else:
            # raise Exception("No se pueden comparar a igualdad los tipos: " + a + " y " + b)
            self.__errores.append("No se pueden comparar a igualdad los tipos: " 
                + a + " y " + b + " en el renglon: " + str(AnalizadorLexico.RENGLON_ACTUAL))

    # Metodo para obtener los errores
    def getErrores(self):
        return self.__errores
        