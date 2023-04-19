class Nodo:
    def __init__(self,posicion,tamaño):
        self.__posicion = posicion
        self.__tamaño = tamaño
        self.__siguiente = None

    def getSiguiente(self):
        return self.__siguiente
    
    def setSiguiente(self,sig):
        self.__siguiente = sig

    def getValor(self):
        return self.__posicion
class Lista:
    def __init__(self):
        self.__cabeza = None
        self.__tamaño = 0
    
    def estaVacia(self):
        self.__cabeza == None

    def anterior(self,posicion):
        if self.estaVacia():
            print('Esta Vacia')
        else:
            anterior = None
            bandera = False
            nodo = self.__cabeza
            while nodo != None and bandera == False:
                if posicion > nodo.getValor():
                    bandera = True
                    anterior = nodo
                nodo = nodo.getSiguiente
            return anterior

    def insertar(self,posicion, tamaño):
        nodo = Nodo(posicion,tamaño)
        if self.__cabeza == None:
            nodo.setSiguiente(self.__cabeza)
            self.__cabeza = nodo
        elif self.__cabeza.getValor() > posicion:
            nodo.setSiguiente(self.__cabeza)
            self.__cabeza = nodo
        else:
            previo=self.anterior(posicion)
            nodo.setSiguiente(previo.getSiguiente)
            previo.setSiguiente(nodo)

    """def recuperar(self,posicion):
        pos=1
        nodo = self.__comienzo
        bandera = False
        aux = None
        if posicion > self.__tamaño:
            aux = -1
        else:
            while nodo != None and bandera == False:
                if pos == posicion:
                    aux = nodo.getValor()
                    bandera = True
                pos+=1
                nodo=nodo.getSiguiente()
        return aux"""

    def recorrer(self):
        if self.estaVacia():
            raise('Esta Vacia')
        nodo = self.__cabeza
        while nodo!=None:
            print(nodo.getValor())
            nodo = nodo.getSiguiente()


if __name__ == '__main__':
    lista = Lista()
    lista.insertar(8,100)
    lista.insertar(4,600)
    lista.insertar(2,400)
    lista.insertar(1,900)

    lista.recorrer()
