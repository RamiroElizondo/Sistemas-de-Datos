import numpy as np
class HashingDA:
    __arreglo: np.array
    __dimension: int

    def __init__(self, dimension):
        self.__dimension = dimension
        self.__arreglo = np.full(dimension, None)
    
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

    def cuadradoMedio(self, valor):
        valor = valor ** 2
        valor = self.metodoDiv(valor)
        valor = self.metodoDiv(valor)
        return valor

    def Alfanumerio(self,cadena):
        total=0
        for caracter in cadena:
            digito = ord(caracter)
            total += digito
        return self.metodoDiv(total)
    
    def insertar(self,valor):
        indice = self.cuadradoMedio(valor)
        print(indice)
        if self.__arreglo[indice] == None:
            self.__arreglo[indice] = valor
        else:
            bandera = False
            while bandera == False:
                indice += 1
                if indice == self.__dimension:
                    indice = 0
                if self.__arreglo[indice] == None:
                    bandera = True
            self.__arreglo[indice] = valor

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
    if primo(tam) == False:
        tam = primoProximo(tam)
    hash = HashingDA(tam)
    print(hash.getArreglo())
    
    hash.insertar(25453)
    hash.insertar(81235)
    hash.insertar(39000)
    hash.insertar(81235)
    hash.insertar(81235)
    hash.insertar(39000)
    hash.insertar(25453)
    
    print(hash.getArreglo())
         