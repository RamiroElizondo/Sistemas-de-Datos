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
    
class PilaE:
    def __init__(self):
        self.__tope = None
        self.__tamaño = 0

    def estaVacia(self):
        return self.__tope == None
    
    def insertar(self,valor):
        nodo = Nodo(valor)
        nodo.setSiguiente(self.__tope)
        self.__tope = nodo
        self.__tamaño +=1
    
    def suprimir(self):
        if self.estaVacia():
            print('Esta Vacia')
            return 0
        else:
            valor = self.__tope
            self.__tope = self.__tope.getSiguiente()
            self.__tamaño-=1
            return valor
    
    def recorrer(self):
        if self.estaVacia():
            print('Esta Vacia')
        else:
            nodo = self.__tope
            while nodo != None:
                print(nodo.getValor())
                nodo = nodo.getSiguiente()

if __name__ == '__main__':
    pila = PilaE()
    pila.insertar(5)
    pila.insertar(8)
    pila.insertar(1)
    pila.recorrer()
    pila.suprimir()
    pila.recorrer()