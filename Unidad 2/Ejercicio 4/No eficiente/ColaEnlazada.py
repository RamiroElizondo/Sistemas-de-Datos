class Nodo:
    def __init__(self,valor,esperando=0):
        self.__valor = valor
        self.__esperando = esperando
        self.__siguiente = None
    
    def getValor(self):
        return self.__valor
    
    def getEsperando(self):
        return self.__esperando
    
    def setEsperando(self,esperando):
        self.__esperando = esperando

    def getSiguiente(self):
        return self.__siguiente
    
    def setSiguiente(self,siguiente):
        self.__siguiente = siguiente
    


class Cola:

    def __init__(self):
        self.__primero = None
        self.__ultimo = None
        self.__tamaño = 0
    
    def insertar(self,valor):
        nodo = Nodo(valor)

        if self.__primero == None:
            self.__primero = nodo
            self.__ultimo = nodo
        
        else:
            self.__ultimo.setSiguiente(nodo)
            self.__ultimo = nodo
    
        self.__tamaño +=1

    def suprimir(self):
        if self.estaVacia():
            return ('Esta Vacia')
        else:
            nodo = self.__primero
            self.__primero = nodo.getSiguiente()
            self.__tamaño -=1
            return nodo
    
    def mostrar(self):
        if self.estaVacia():
           return ('Esta Vacia')
        else:
            nodo = self.__primero
            while nodo.getSiguiente() != None:
                print(nodo.getValor())
                nodo = nodo.getSiguiente()
            print(nodo.getValor())
    
    def mostrarE(self):
        if self.estaVacia():
           return ('Esta Vacia')
        else:
            nodo= self.__primero
            while nodo.getSiguiente() != None:
                print(nodo.getEsperando())
                nodo = nodo.getSiguiente()
            print(nodo.getEsperando())
    
    def estaVacia(self):
        return self.__tamaño == 0
    
    def getTamaño(self):
        return self.__tamaño
    
    def recorrer(self): 

        if self.estaVacia() == True:
            return 0
        else:
            acum:int = 0
            nodo = self.__primero
            while nodo.getSiguiente() != None:
                acum += nodo.getEsperando()
                nodo = nodo.getSiguiente()
            acum += nodo.getEsperando()
            return acum
    
    def aumentarValores(self):
        if not self.estaVacia():
            
            nodo = self.__primero

            while nodo.getSiguiente() is not None:
                valor = nodo.getEsperando()
                valor+=1
                nodo.setEsperando(valor)
                nodo = nodo.getSiguiente()
            

            valor = nodo.getEsperando()
            valor+=1
            nodo.setEsperando(valor)