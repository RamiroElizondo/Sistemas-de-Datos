import numpy as np
class ListaSContenido:
    __tamaño:int
    __tope:int

    def __init__(self,tamaño):
        self.__tamaño = tamaño
        self.__tope = 0
        self.__arreglo = np.full(tamaño,0,dtype=int)

    def estaVacia(self):
        return self.__tope == 0

    def shifteo(self,pos):
        indice = self.__tope-1
        while indice >=pos:
            self.__arreglo[indice+1] = self.__arreglo[indice]
            indice-=1
    
    def insertar(self,valor):
        if self.__tope >= self.__tamaño:
            raise('Lista llena')
        if self.estaVacia():
            self.__arreglo[self.__arreglo] = valor
        else:
            bandera = False
            i = 0
            while i < self.__tope and bandera == False:
                if valor < self.__arreglo[i]:
                    self.shifteo(i)
                    self.__arreglo[i] = valor
                    bandera = True
                i+=1
        self.__tope+=1
    
    def buscar(self,valor):
        inferior = 0
        superior = self.__tamaño
        m= int((inferior+superior)/2)

        while inferior <= superior and valor != self.__arreglo[m]:
            if valor < self.__arreglo[m]:
                superior = m-1
            else:
                inferior = m+1
            m= int((inferior+superior)/2)
        if inferior > superior:
            print('No esta')
        else:
            print('Si esta y su posicion es: ',m+1)
    def recorrer(self):
        print(self.__arreglo)
if __name__ == '__main__':
    lista = ListaSContenido(5)
    lista.insertar(20)
    lista.insertar(1)
    lista.insertar(10)
    lista.insertar(7)
    lista.insertar(6)
    lista.recorrer()
    lista.buscar(20)