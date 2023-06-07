import numpy as np


class Nodo:
    __valor = None
    __siguiente = None
    
    def __init__(self, valor):
        self.__valor = valor
        self.__siguiente = None
        
    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente
    
    def getSiguiente(self):
        return self.__siguiente

    def getValor(self):
        return self.__valor

class Hashing:
    __arreglo = None
    __dimension = None
    __cantPreguntas: int
    def __init__(self,dimension):
        self.__dimension = dimension
        self.__arreglo = np.full(dimension, None)
        self.__cantPreguntas = 0
    def getArreglo(self):
        return self.__arreglo

    def metodoDiv(self, valor):
        valor = valor % self.__dimension
        return valor
    
    def extraccion(self, valor,mod=10):
        valor =(valor) % mod
        return valor

    def plegado(self, valor): #25 %5 /10 2.5
        suma = 0
        while valor > 0:
            suma += valor % 100
            valor = valor // 100
        return self.metodoDiv(suma)

    def cuadrado_medio(self, valor):
        potencia = valor ** 2
        cadena = str(potencia)
        medios = cadena[len(cadena)//2-1:(len(cadena)//2+1)+1]
        indice = int(medios) % self.__dimension
        return indice

    def Alfanumerio(self,cadena):
        total=0
        for caracter in cadena:
            digito = ord(caracter)
            total += digito
        return self.metodoDiv(total)

    def insertar2(self, valor):
        indice = self.plegado(valor)
        print(indice)

        nodo = Nodo(valor)
        if self.__arreglo[indice] == None:
            self.__arreglo[indice] = nodo
        else:
            nodo.setSiguiente(self.__arreglo[indice])
            self.__arreglo[indice] = nodo

    def insertar(self,valor):
        indice = self.metodoDiv(valor)
        nodo = Nodo(valor)
        if self.__arreglo[indice] == None:
            self.__arreglo[indice] = nodo
        else:
            nodo.setSiguiente(self.__arreglo[indice])
            self.__arreglo[indice] = nodo

    def buscar(self,valor):
        indice = self.plegado(valor)
        actual = self.__arreglo[indice]
        bandera = False
        if actual is None:
            self.__cantPreguntas+=1
            print('No esta')
        else:
            while actual != None and bandera != True:
                self.__cantPreguntas+=1
                if actual.getValor() == valor:
                    print('El elemento si esta')
                    bandera = True
                actual = actual.getSiguiente()

    def getArreglo(self):
        return self.__arreglo
def primo(valor):
    bandera = True
    for i in range(2,valor):
        if valor % i == 0:
            bandera = False
    return bandera

def primoProximo(valor):
    while primo(valor) == False:
        valor += 1
    return valor

if __name__ == '__main__':
    tam = int(input('Ingrese el tamaño del arreglo: '))
    tam//=2
    if primo(tam) == False:
        tam = primoProximo(tam)
    print('Tamaño',tam)

    # Tamaño ingresado: 461, luego queda en 233
    # Para la primer clave, los numeros centrales son 855
    # Para la segunda clave, los numeros centrales son 125 

    hash = Hashing(tam)
    hash.insertar2(25453)
    hash.insertar2(81235)
    hash.buscar(25453)
    arreglo = hash.getArreglo()
    for i in range(len(arreglo)):
        if arreglo[i] != None:
            print(i,arreglo[i].getValor())
    #hash.buscar(25453,1)