class Nodo:
    def __init__(self,valor):
        self.__valor = valor
        self.__siguiente = None
    
    def getValor(self):
        return self.__valor
    
    def getSiguiente(self):
        return self.__siguiente
    
    def setSiguiente(self,sig):
        self.__siguiente = sig

class ColaE:
    __cabeza: Nodo
    __cola: Nodo
    __cant:int

    def __init__(self):
        self.__cabeza = None
        self.__cola = None
        self.__cant = 0

    def estaVacia(self):
        return self.__cabeza == None

    def insertar(self,valor):
        nodo = Nodo(valor)
        if self.estaVacia():
            self.__cabeza = nodo
            self.__cola = nodo
        else:
            self.__cola.setSiguiente(nodo)
            self.__cola=nodo
        
    def suprimir(self):
        if self.estaVacia():
            print('No quedan elementos')
            return 0
        else:  
            nodo = self.__cabeza
            self.__cabeza = self.__cabeza.getSiguiente()
            return nodo
    
    def recorrer(self):
        if self.estaVacia():
            print('No quedan elementos')
            return 0
        else:  
            nodo = self.__cabeza
            while nodo != None:
                print(nodo.getValor())
                nodo = nodo.getSiguiente()

if __name__ == '__main__':
    cola = ColaE()
    cola.insertar(5)
    cola.insertar(7)
    cola.insertar(8)
    cola.suprimir()
    cola.recorrer()