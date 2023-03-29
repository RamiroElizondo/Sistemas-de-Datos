import numpy as np

class Cola:
    __elementos: np.ndarray
    __indice = 0
    __tamaño = 0

    def __init__(self,tamaño):
        self.__elementos = np.full(tamaño,0)
        self.__indice = 0
        self.__tamaño = tamaño

    def insertar(self, valor):
        if self.__indice == self.__tamaño:
            raise('Cola llena')
        self.__elementos[self.__indice] = valor
        self.__indice +=1
    
    def suprimir(self):
        if self.__indice == 0:
            raise('Ya no quedan elementos')
        valor = self.__elementos[0]

        for i in range(1,self.__indice):
            self.__elementos[i-1] = self.__elementos[i]
        self.__elementos[i]=0
        self.__indice -= 1

        return valor

    def estaVacia(self):
        return self.__indice == 0

    def mostrar(self):
        if self.estaVacia():
            raise('Esta Vacia')
        
        for i in range(self.__tamaño):
            print(self.__elementos[i])

   
if __name__ == '__main__':
    cola = Cola(4)
    cola.insertar(2)
    cola.insertar(3)
    cola.insertar(4)
    cola.insertar(5)
    cola.mostrar()
    print('\n')
    valor = cola.suprimir()
    print(valor)
    print('\n')
    cola.mostrar()
    