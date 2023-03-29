import numpy as np

class Pila:
    __elementos: np.ndarray
    __tamaño:int 

    def __init__(self,tamaño:int = 10):
        self.__elementos = np.full(tamaño,' ')
        self.__tope = 0
        self.__tamaño = tamaño
    
    def esta_vacia(self):
        return self.__tope == 0
    
    def insertar(self, valor):
        if self.__tope == self.__tamaño:
            raise('Pila llena')
        self.__elementos[self.__tope] = valor
        self.__tope += 1 #Aumentamos el tamaño de la pila
        
    
    def suprimir(self):
        if self.esta_vacia():
            raise("Pila vacía")
        
        valor = self.__elementos[self.__tope-1]
        self.__elementos[self.__tope-1] = ' '
        self.__tope -= 1
        return valor

    def mostrar(self):
        if self.esta_vacia():
            raise("Pila vacía")
        
        for i in self.__elementos:
            print(i)

    def getElementos(self):
        return self.__elementos

    def getTope(self):
        return self.__tope
    
    def getTamaño(self):
        return self.__tamaño
