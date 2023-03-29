import numpy as np

class Pila:
    __elementos: np.ndarray
    __tope:int 
    __tamaño:int 

    def __init__(self,tamaño:int = 10):
        self.__elementos = np.full(tamaño,1)
        self.__tope = 0
        self.__tamaño = tamaño
    
    def esta_vacia(self):
        return self.__tope is None
    
    def insertar(self, valor):
        if self.__tope == self.__tamaño:
            raise('Pila llena')
        self.__elementos[self.__tope] = valor
        self.__tope += 1 #Aumentamos el tamaño de la pila
    
    def suprimir(self):
        if self.esta_vacia():
            raise("Pila vacía")
        valor = self.__elementos[self.__tope]
        print(self.__tope)
        self.__tope -= 1
        return valor

    def mostrar(self):
        if self.esta_vacia():
            raise("Pila vacía")
        
        for i in self.__elementos:
            print(i)



if __name__ == '__main__':
    numero = int(input('Ingrese un numero: '))
    pila = Pila(numero)
    valor = numero
    resultado = 1
    while numero != 0:
        pila.insertar(numero)
        numero -= 1
    
    pila.mostrar()
    while not pila.esta_vacia():
        resultado = resultado * pila.suprimir()

    print('El factorial de', valor, 'es', resultado)