import numpy as np
class Nodo:
    def __init__(self,valor=0):
        self.__valor = valor
    
    def getValor(self):
        return self.__valor

class ColaC:
    __tamaño:int
    __primero: int
    __ultimo : int
    __cant: int

    def __init__(self,tamaño):
        self.__tamaño = tamaño
        self.__primero = 0
        self.__ultimo = 0
        self.__cant = 0
        self.__arreglo = np.full(tamaño,0,dtype=Nodo)

    def estaVacia(self):
        return self.__cant==0

    def insertar(self,valor):
        nodo= Nodo(valor)
        if self.__cant < self.__tamaño:
            mostrar = 'Se ingreso correctamente'+str(self.__ultimo)
            self.__arreglo[self.__ultimo] = nodo
            self.__ultimo = (self.__ultimo+1)%self.__tamaño
            self.__cant+=1
           
        return print(mostrar)

    def suprimir(self):
        if self.estaVacia():
            valor = 0
        else:
            valor = self.__arreglo[self.__primero].getValor()
            self.__primero = (self.__primero+1)%self.__tamaño
            self.__cant-=1
        return valor

    def mostrar(self):
        if self.estaVacia():
            mostrar = 'Cola Vacia'
        else:
            i = self.__primero
            j=0
            for j in range(self.__cant):
                print(self.__arreglo[i].getValor())
                i=(i+1)%self.__tamaño
            mostrar = ''
        return print(mostrar)

    
if __name__ == '__main__':
    cola = ColaC(5)
    cola.insertar(10)
    cola.insertar(4)
    cola.insertar(8)
    cola.insertar(2)
    cola.insertar(29)
    cola.mostrar()
    cola.suprimir()
    cola.insertar(7)
    cola.mostrar()
    cola.suprimir()
    cola.insertar(100)
    cola.mostrar()

