class Nodo:
    def __init__(self,valor,esperando=0):
        self.__valor = valor
        self.__esperando = esperando
        self.__siguiente = None

    def getValor(self):
        return self.__valor
    
    def setValor(self,valor):
        self.__valor = valor

    def getSiguiente(self):
        return self.__siguiente
    
    def setSiguiente(self,sig):
        self.__siguiente = sig

    def getEspernado(self):
        return self.__esperando
    
    def setEsperando(self,esperando):
        self.__esperando = esperando

class Cola:
    def __init__(self):
        self.__primero = None
        self.__ultimo = None
        self.__tamaño = 0

    def insertar(self,valor):
        nodo = Nodo(valor)
        if self.__primero == None:
            self.__primero = nodo
            self.__cola = nodo
        else:
            self.__cola.setSiguiente(nodo)
            self.__cola = nodo   
        self.__tamaño +=1

    def suprimir(self):
        if self.estaVacia():
            return 'Ya no quedan elementos'
        else:
            nodo = self.__primero
            self.__primero = nodo.getSiguiente()
            self.__tamaño -=1
            return nodo

    def estaVacia(self):
        return self.__primero == None and self.__ultimo == None
