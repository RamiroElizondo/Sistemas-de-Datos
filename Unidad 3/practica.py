class Nodo:
    __valor: int
    """__izquierda: None|Nodo
    __derecha: None|Nodo"""

    def __init__(self,valor):
        self.__valor = valor
        self.__contador = 1
        self.__izquierda = None
        self.__derecha = None

    def getValor(self):
        return self.__valor

    def setValor(self,valor):
        self.__valor = valor

    def getIzquierda(self):
        return self.__izquierda
    
    def setIzquierda(self,iz):
        self.__izquierda = iz
    
    def getDerecha(self):
        return self.__derecha
    
    def setDerecha(self,de):
        self.__derecha = de
    
    def getContador(self):
        return self.__contador

    def setContador(self):
        self.__contador +=1

class ArbolBB:
    __raiz: None|Nodo

    def __init__(self):
        self.__raiz = None
    
    def esta_vacio(self):
        return self.__raiz == None

    def insertar(self,valor):
        nodo = Nodo(valor)
        if self.esta_vacio():
            self.__raiz = nodo
        else:
            self.insertarRecursivo(nodo,self.__raiz)
    
    def insertarRecursivo(self,nodo,nodoActual):
        if nodo.getValor() < nodoActual.getValor():
            if nodoActual.getIzquierda() is None:
                nodoActual.setIzquierda(nodo)
            else:
                self.insertarRecursivo(nodo,nodoActual.getIzquierda())
        elif nodo.getValor() > nodoActual.getValor():
            if nodoActual.getDerecha() is None:
                nodoActual.setDerecha(nodo)
            else:
                self.insertarRecursivo(nodo, nodoActual.getDerecha())
        else:
            print('El elemento ya esta en la lista')
            nodoActual.setContador()
    
    def suprimir(self,valor):
        if not self.esta_vacio():
            self.__raiz = self.suprimirRecusivo(valor,self.__raiz)
        else:
            print('Arbol Vacio')
    
    def suprimirRecusivo(self,valor,nodoActual):
        if valor == nodoActual.getValor():
            if nodoActual.getIzquierda() is None and nodoActual.getDerecha() is None:
                return None

            if nodoActual.getIzquierda() != None and nodoActual.getDerecha() == None:
                return nodoActual.getIzquierda()
            elif nodoActual.getIzquierda() == None and nodoActual.getDerecha() != None:
                return nodoActual.getDerecha()
            
            reemplazo = self.reemplazo(nodoActual.getIzquierda())
            nodoActual.setValor(reemplazo.getValor())
            
            nodoActual.setIzquierda(self.suprimirRecusivo(reemplazo.getValor(),nodoActual.getIzquierda()))
        elif valor < nodoActual.getValor():
            nodoActual.setIzquierda(self.suprimirRecusivo(valor,nodoActual.getIzquierda()))
        elif valor > nodoActual.getValor():
            nodoActual.setDerecha(self.suprimirRecusivo(valor, nodoActual.getDerecha()))
        return nodoActual
    
    def reemplazo(self,nodo):
        if nodo.getDerecha() is not None:
            return self.reemplazo(nodo.getDerecha())
        return nodo
    def getRaiz(self):
        return self.__raiz
    
    def inOrden2(self,nodo):
        if nodo != None:
            self.inOrden2(nodo.getIzquierda())
            print(nodo.getValor(),',',end='')
            self.inOrden2(nodo.getDerecha())
    
    def preOrden(self,nodo):
        if nodo != None:
            print(nodo.getValor(),',',end='')
            self.inOrden2(nodo.getIzquierda())
            self.inOrden2(nodo.getDerecha())
    
    def postOrden(self,nodo):
        if nodo != None:
            self.inOrden2(nodo.getIzquierda())
            self.inOrden2(nodo.getDerecha())
            print(nodo.getValor(),',',end='')

if __name__ == '__main__':
    arbol = ArbolBB()
    arbol.insertar(12)
    arbol.insertar(7)
    arbol.insertar(16)
    arbol.insertar(3)
    arbol.insertar(9)
    arbol.insertar(14)
    """print(arbol.getRaiz().getValor())
    print(arbol.inOrden(arbol.getRaiz()))"""


    print(arbol.getRaiz().getValor())
    arbol.inOrden2(arbol.getRaiz())
    print('\n')
    arbol.preOrden(arbol.getRaiz())
    print('\n')
    arbol.postOrden(arbol.getRaiz())
