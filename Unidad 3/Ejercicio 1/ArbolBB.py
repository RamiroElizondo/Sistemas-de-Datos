from __future__ import annotations
import numpy as np

class Nodo:
    __valor: int
    __izquierda: Nodo | None
    __derecha: Nodo | None

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

    def setContador(self,valor):
        self.__contador = valor
    
    def grado(self):
        if self.__izquierda == None and self.__derecha == None:
            return 0
        elif self.__izquierda == None or self.__derecha == None:
            return 1
        else:
            return 2

class ArbolBB:
    __raiz: None|Nodo

    def __init__(self):
        self.__raiz = None

    def getRaiz(self):
        return self.__raiz

    def insertar(self,valor):
        nodo = Nodo(valor)
        if self.__raiz == None:
            self.__raiz = nodo
        else:
            self.insertarRecursivo(nodo,self.__raiz)
    
    def insertarRecursivo(self,nodo,nodoActual):
        if nodo.getValor() == nodoActual.getValor():
            print('El elemento ya esta en la lista')
            valor = nodoActual.getContador()
            nodoActual.setContador(valor+1)
            return 
        if nodo.getValor() < nodoActual.getValor():
            if nodoActual.getIzquierda() is None:
                nodoActual.setIzquierda(nodo)
            else:
                self.insertarRecursivo(nodo,nodoActual.getIzquierda())
        else:
            if nodoActual.getDerecha() is None:
                nodoActual.setDerecha(nodo)
            else:
                self.insertarRecursivo(nodo, nodoActual.getDerecha())

    def suprimir(self,valor):
        if self.__raiz != None:
            self.__raiz = self.suprimirRecursivo(valor,self.__raiz)
        else:
            print('Arbol Vacio')

    def reemplazo(self,nodo):
        if nodo.getDerecha() is not None:
            return self.reemplazo(nodo.getDerecha())
        return nodo
    
    def suprimirRecursivo(self,valor,nodoActual,anterior= Nodo|None,izquierda=True):
        if valor == nodoActual.getValor():
            if nodoActual.getContador() > 1:
                valor = nodoActual.getContador()
                nodoActual.setContador(valor-1)

            elif self.hoja(nodoActual): #Si es hoja
                if izquierda: 
                    anterior.setIzquierda(None) #Si el nodo hoja es hijo izquierdo
                else: 
                    anterior.setDerecha(None) #Si el nodo hoja es hijo derecho
            elif nodoActual.grado() == 1: #Si tiene un hijo+
                if nodoActual.getIzquierda() is not None: 
                    hijo = nodoActual.getIzquierda() #Si el hijo es izquierdo
                else:
                    hijo = nodoActual.getDerecha() #Si el hijo es derecho 
                if izquierda: 
                    anterior.setIzquierda(hijo)
                else:
                    anterior.setDerecha(hijo)
            elif nodoActual.grado() == 2: #Si tiene dos hijos
                reemplazo = self.reemplazo(nodoActual.getIzquierda())
                nodoActual.setValor(reemplazo.getValor())
                self.suprimirRecursivo(reemplazo.getValor(),nodoActual.getIzquierda(),nodoActual,True)
        elif valor < nodoActual.getValor():
            if nodoActual.getIzquierda() is not None:
                self.suprimirRecursivo(valor,nodoActual.getIzquierda(),nodoActual,True)
        else:
            if nodoActual.getDerecha() is not None:
                self.suprimirRecursivo(valor,nodoActual.getDerecha(),nodoActual,False)
        return nodoActual 

    def buscar(self,valor,nodoActual):
        if valor == nodoActual.getValor():
            return nodoActual
        elif valor < nodoActual.getValor():
            if nodoActual.getIzquierda() != None:
                return self.buscar(valor, nodoActual.getIzquierda())
            else:
                return False
        elif valor > nodoActual.getValor():
            if nodoActual.getDerecha() != None:
                return self.buscar(valor,nodoActual.getDerecha())
            else:
                return False

    def nivel(self,nodo,nodoActual,contador):
        if nodo.getValor() == nodoActual.getValor():
            return contador
        elif nodo.getValor() < nodoActual.getValor():
            if nodoActual.getIzquierda() != None:
                contador += 1
                return self.nivel(nodo,nodoActual.getIzquierda(),contador)
        elif nodo.getValor() > nodoActual.getValor():
            if nodoActual.getDerecha() != None:
                contador += 1
                return self.nivel(nodo,nodoActual.getDerecha(),contador)

    def hoja(self,nodo):
        if nodo.getDerecha() == None and nodo.getIzquierda() == None:
            return True
        else:
            return False

    def hijo(self,hijo,padre):
        if padre.getValor() == hijo.getValor():
            return True
        elif padre.getValor() > hijo.getValor():
            if padre.getIzquierda() != None:
                return self.hijo(hijo,padre.getIzquierda())
            else:
                return False
        elif padre.getValor() < hijo.getValor():
            if padre.getDerecha() != None:
                return self.hijo(hijo,padre.getDerecha())
            else:
                return False
        
    def padre(self,hijo,padre):
        return self.hijo(hijo, padre)

    def camino(self,desde,hasta,arreglo):
        if desde.getValor() == hasta.getValor():
            arreglo.append(desde.getValor())
            return arreglo
        elif desde.getValor() < hasta.getValor():
            arreglo.append(desde.getValor())
            return self.camino(desde.getDerecha(),hasta,arreglo)
        elif desde.getValor() > hasta.getValor():
            arreglo.append(desde.getValor())
            return self.camino(desde.getIzquierda(),hasta,arreglo)

    def altura(self, nodo):
        if nodo is None:
            return 0
        else:
            alturaIzq = self.altura(nodo.getIzquierda())
            alturaDer = self.altura(nodo.getDerecha())
            return max(alturaIzq, alturaDer) + 1

    def inOrden(self,nodo):
        if nodo != None:
            self.inOrden(nodo.getIzquierda())
            print(nodo.getValor(),' ',end='')
            self.inOrden(nodo.getDerecha())

    def preOrden(self,nodo):
        if nodo != None:
            print(nodo.getValor(),' ',end='')
            self.preOrden(nodo.getIzquierda())
            self.preOrden(nodo.getDerecha())

    def postOrden(self,nodo):
        if nodo != None:
            self.postOrden(nodo.getIzquierda())
            self.postOrden(nodo.getDerecha())
            print(nodo.getValor(),' ',end='')
        
    def cantHojas(self,nodo,contador):
        if nodo != None:
            if self.hoja(nodo):
                contador += 1
            contador = self.cantHojas(nodo.getIzquierda(),contador)
            contador = self.cantHojas(nodo.getDerecha(),contador)
        return contador
    
    def antecesores(self, nodo, valor, arreglo,indice=0):
        if nodo != None:
            if nodo.getValor() == valor:
                return arreglo
            else:
                arreglo[indice] = nodo.getValor()
                indice+=1
                if nodo.getValor() > valor:
                    return self.antecesores(nodo.getIzquierda(), valor, arreglo,indice)
                else:
                    return self.antecesores(nodo.getDerecha(), valor, arreglo,indice)
        else:
            return arreglo