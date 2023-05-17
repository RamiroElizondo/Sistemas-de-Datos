import numpy as np
from pila import Pila

class Nodo:
    __siguiente = None
    __valor = None

    def __init(self, valor):
        self.__siguiente = None
        self.__valor = None
    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente
    def getDato(self):
        return self.__valor
    def getSigiuente(self):
     return self.__siguiente

class Hashing:
    __arreglo = None
    __dimension = None
    __cantColisiones = None
    def __init__(self,dimension):
        self.__dimension = dimension
        self.__arreglo = np.full(dimension, Pila(), dtype=Pila)
        self.__cantColisiones = None

    def metodoDiv(self, valor):
        valor = valor % self.__dimension
        return valor
    
    def extraccion(self, valor,mod=10):
        valor =(valor) % mod
        return valor

    def plegado(self, valor): #25 %5 /10 2.5
        suma = 0
        while valor > 0:
            suma += valor % 10
            valor = valor // 10
        return suma

    def cuadradoMedio(self, valor):
        valor = valor ** 2
        valor = self.extraccion(valor,100)
        return valor

    def Alfanumerio(self,cadena):
        total=0
        for caracter in cadena:
            digito = ord(caracter)
            total += digito
        total = total % self.__dimension
        return total

    def insertar(self,valor): #5
        indice = self.metodoDiv(valor)
        print('1',indice)
        indice = self.extraccion(valor)
        print('2',indice)
        indice = self.plegado(valor)
        print('3',indice)
        indice = self.cuadradoMedio(valor)
        print('4',indice)
        print('\n')

        #self.__arreglo[indice].Linsetar(valor)
    
    def insertarA(self,valor):
        indice = self.Alfanumerio(valor)
        print(indice)

if __name__ == '__main__':
    hash = Hashing(50)
    """hash.insertar(25453)
    hash.insertar(81235)"""
    hash.insertarA('hola')