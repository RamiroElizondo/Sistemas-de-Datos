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
            print('Me inserte en la cabeza')
        else:
            self.__cola.setSiguiente(nodo)
            self.__cola = nodo
            print('Me inserte en la cola')
        
        
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
    
    def mostrar(self):
        nodo = self.__primero
        if self.estaVacia():
            return 'Esta vacia'

        while nodo.getSiguiente() is not None:
            print('Le quedan {} minutos'.format(nodo.getValor()))
            nodo = nodo.getSiguiente()
        print('Le quedan {} minutos'.format(nodo.getValor()))

    def aumentarValores(self):
        if self.estaVacia():
            return print('Esta vacia')
        nodo = self.__primero

        while nodo.getSiguiente() is not None:
            valor = nodo.getEspernado()
            valor+=1
            nodo.setEsperando(valor)
            nodo = nodo.getSiguiente()
        
        valor = nodo.getEspernado()
        valor+=1
        nodo.setEsperando(valor)

if __name__ == '__main__':
    cola = Cola()
    i=0
    cola.insertar(2,i+1)
    i+=1
    cola.insertar(3,i+1)
    i+=1
    cola.insertar(4,i+1)
    i+=1
    cola.mostrar()
    print('\n')
    valor = cola.suprimir()
    print(valor.getValor())
    print('\n')
    cola.mostrar()
