class Nodo:
    def __init__(self,valor,numero,esperando=0):
        self.__numeroT = numero
        self.__valor = valor
        self.__esperando = esperando
        self.__siguiente = None

    def getValor(self):
        return self.__valor
    
    def getSiguiente(self):
        return self.__siguiente
    
    def setSiguiente(self,sig):
        self.__siguiente = sig
    
    def setValor(self,valor):
        self.__valor = valor
    
    def aumentarEspera(self):
        self.__esperando +=1

    def getEspernado(self):
        return self.__esperando
    
    def setEsperando(self,esperando):
        self.__esperando = esperando
    def getNumero(self):
        return self.__numeroT
    

class Cola:

    def __init__(self):
        self.__cabeza = None
        self.__cola = None
        self.__tamaño = 0

    def insertar(self,valor,numero):
        nodo = Nodo(valor,numero)
        print('Entre al insertar')
        if self.__cola == None:
            self.__cabeza = nodo
            print(nodo)
            print('Cola es none, asi que entre aca')
        else:
            print('ahora entre aca')
            self.__cola.setSiguiente(nodo)
        
        self.__cola = nodo
        self.__tamaño +=1

    def suprimir(self):
        if self.__cabeza == None:
            raise('Ya no quedan elementos')
        nodo = self.__cabeza

        self.__cabeza = nodo.getSiguiente()
        self.__tamaño -=1
        return nodo

    def estaVacia(self):
        return self.__tamaño == 0
    
    def mostrar(self):
        if self.estaVacia():
            raise('Esta vacia')
        nodo = self.__cabeza

        while nodo.getSiguiente() is not None:
            print('Trabajo: {} le quedan {} minutos'.format(nodo.getNumero(),nodo.getValor()))
            nodo = nodo.getSiguiente()
    

        print('Trabajo: {} le quedan {} minutos'.format(nodo.getNumero(),nodo.getValor()))

    def aumentarValores(self):
        nodo = self.__cabeza
        

        if self.__cabeza == self.__cola:
            nodo.aumentarEspera()
        else:
            while nodo.getSiguiente() is not None:
                nodo.aumentarEspera()
                nodo = nodo.getSiguiente()
            nodo.aumentarEspera()

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
