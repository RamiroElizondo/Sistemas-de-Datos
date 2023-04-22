import numpy as np
class PilaS:
    __tamaño = 0
    __tope = -1
    def __init__(self,tamaño):
        self.__tamaño = tamaño
        self.__tope
        self.__arreglo = np.full(tamaño,0,dtype=int)

    def estaVacia(self):
        return self.__tope == -1
    
    def insertar(self,valor):
        if self.__tope < self.__tamaño-1:
            self.__tope+=1
            self.__arreglo[self.__tope] = valor
            valor = 'Se inserto'
        else:
            valor = 'Esta llena'
        return print(valor)
    
    def suprimir(self):
        if self.estaVacia():
            return(0)
        else:
            valor = self.__arreglo[self.__tope]
            self.__tope-=1
            return valor
        
    def recorrer(self):
        i=0
        for i in range(self.__tope,-1,-1): #Parametro 1: cantidad del arreglo, Parametro 2: Indica que va ir disminuyendo hasta antes de -1, Parametro 3: indica que disminuye en 1 en 1
            print(self.__arreglo[i])

if __name__ == '__main__':
    pila = PilaS(5)
    pila.insertar(4)
    pila.insertar(5)
    pila.insertar(6)
    pila.suprimir()
    pila.recorrer()
    