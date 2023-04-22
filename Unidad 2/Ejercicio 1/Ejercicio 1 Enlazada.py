"""
Escribir una función en que simule el funcionamiento del stack de recursión, durante la ejecución de la
función Factorial, que calcula el factorial de un número según: n ! = n * (n – 1) ! si n > 0
n ! = 1 , si n = 0
"""

class Nodo:
    def __init__(self, valor):
        self.__valor = valor
        self.__siguiente = None

    def setSiguiente(self,siguiente):
        self.__siguiente = siguiente

    def getSiguiente(self):
        return self.__siguiente
    
    def getValor(self):
        return self.__valor

class Pila:
    def __init__(self):
        self.__tope = None
        self.__tamaño = 0
    
    def esta_vacia(self):
        return self.__tope is None
    
    def insertar(self, valor):
        nuevo_nodo = Nodo(valor) #Creamos el nodo
        nuevo_nodo.setSiguiente(self.__tope) #El siguiente del nodo es el tope
        self.__tope = nuevo_nodo #El tope es el nodo
        self.__tamaño += 1 #Aumentamos el tamaño de la pila
    
    def suprimir(self):
        if self.esta_vacia():
            print("Pila vacía")
            return None
        valor = self.__tope.getValor() #Guardamos el valor del tope para saber que valor vamos a eliminar
        self.__tope = self.__tope.getSiguiente()
        self.__tamaño -= 1
        return valor

    def mostrar(self):
        if self.esta_vacia():
            print("Pila vacía")
            return None
        nodo = self.__tope
        while nodo.getSiguiente() is not None:
            print(nodo.getValor())
            nodo = nodo.getSiguiente()
        print(nodo.getValor())



if __name__ == '__main__':
    pila = Pila()
    numero = int(input('Ingrese un numero: '))
    valor = numero
    resultado = 1
    while numero != 0:
        pila.insertar(numero)
        numero -= 1
    
    pila.mostrar()
    print('\n')
    while not pila.esta_vacia():
        resultado = resultado * pila.suprimir()
        """pila.mostrar()
        print('\n')"""
        

    print('El factorial de', valor, 'es', resultado)