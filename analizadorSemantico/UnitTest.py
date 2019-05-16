import operator
from ArbolExpresiones import ArbolExpresiones
from Nodo import Nodo
# 3 + (3 - 5)
n = Nodo(None , None, operator.add)
n.setNodoIzquierdo(Nodo(None, None, 3))
n.setNodoDerecho(Nodo(Nodo(None, None, 3), Nodo(None, None, 5), operator.sub))
a = ArbolExpresiones(n,[operator.add , operator.sub, operator.mul])
print(a.solve())