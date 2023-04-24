import numpy as np
class ListaSPosicion:
    __tamaño:int
    __tope:int

    def __init__(self,tamaño):
        self.__tamaño = tamaño
        self.__tope = 0
        self.__arreglo = np.full(tamaño,0,dtype=int)
    
    def estaVacia(self):
        return self.__tope == 0
    
    def shifteo(self,posicion):
        indice = self.__tope-1
        while indice >= posicion:
            self.__arreglo[indice+1] =self.__arreglo[indice]
            indice-=1
            
    def insertar(self,valor,posicion):

        if self.__tope >= self.__tamaño:
            raise('Lista llena')
        if self.estaVacia():
            self.__arreglo[self.__tope] = valor
            self.__tope +=1
        elif self.__tope >= posicion:
            pos=0
            bandera = False
            while bandera==False:
                if pos == posicion:
                    self.shifteo(posicion)
                    self.__arreglo[posicion] = valor
                    bandera = True
                pos+=1
            self.__tope +=1
        else:
            print('La posicion tiene que ser mas chico que el tope')
    def recorrer(self):
        for i in range(self.__tope):
            print(self.__arreglo[i])

    def deshisfteo(self,indice):
        valor = self.__arreglo[indice]
        while indice < self.__tope-1:
            self.__arreglo[indice]= self.__arreglo[indice+1]
            indice+=1
        return valor

    def suprimir(self,posicion):
        if self.estaVacia():
            print('Lista Vacia')
        elif posicion < self.__tope:
            pos = 0
            bandera = False
            while bandera == False:
                if pos == posicion:
                    self.deshisfteo(posicion)
                    bandera = True
                pos+=1
            self.__tope-=1
        else:
            print('Fuera de rango')

if __name__ == '__main__':
    lista = ListaSPosicion(5)
    lista.insertar(6,0)
    lista.insertar(7,1)
    lista.insertar(10,2)
    lista.insertar(20,1)
    lista.insertar(50,4)
    lista.recorrer()
    lista.suprimir(1)
    lista.suprimir(3)
    print('\n')
    lista.recorrer()
    