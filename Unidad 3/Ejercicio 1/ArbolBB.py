class Nodo:
    __valor: int
   

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

    def getRaiz(self):
        return self.__raiz

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
    
    
    def buscar(self,valor,nodoActual):
        if self.esta_vacio():
            return None
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
        elif valor == nodoActual.getValor():
            return nodoActual
    
    def nivel(self,nodo,nodoActual,contador):
        if self.esta_vacio():
            return None
        elif nodo.getValor() < nodoActual.getValor():
            if nodoActual.getIzquierda() != None:
                contador += 1
                return self.nivel(nodo,nodoActual.getIzquierda(),contador)
        elif nodo.getValor() > nodoActual.getValor():
            if nodoActual.getDerecha() != None:
                contador += 1
                return self.nivel(nodo,nodoActual.getDerecha(),contador)
        elif nodo.getValor() == nodoActual.getValor():
            return contador

    def hoja(self,nodo):
        if nodo.getDerecha() == None and nodo.getIzquierda() == None:
            print('El nodo con valor',valor,'es hoja')
            return None
        else:
            print('No es hoja')
            return nodo
        
    def hijo(self,hijo,padre):
        if padre.getIzquierda() != None:
            if padre.getIzquierda().getValor() == hijo.getValor():
                return True
        if padre.getDerecha() != None:
            if padre.getDerecha().getValor() == hijo.getValor():
                return True
        
    def padre(self,hijo,padre):
        return self.hijo(hijo, padre)

    def camino(self,desde,hasta,arreglo):
        if self.esta_vacio():
            return None
        elif desde.getValor() < hasta.getValor():
            arreglo.append(desde.getValor())
            return self.camino(desde.getDerecha(),hasta,arreglo)
        elif desde.getValor() > hasta.getValor():
            arreglo.append(desde.getValor())
            return self.camino(desde.getIzquierda(),hasta,arreglo)
        else:
            arreglo.append(desde.getValor())
            return arreglo

    def altura(self, nodo):
        if nodo is None:
            return 0
        else:
            alturaIzq = self.altura(nodo.getIzquierda())
            alturaDer = self.altura(nodo.getDerecha())
            return max(alturaIzq, alturaDer) + 1
        
                