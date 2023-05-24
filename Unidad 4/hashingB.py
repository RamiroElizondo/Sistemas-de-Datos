import numpy as np
class HashingB:
    __arreglo: np.array
    __tamaño: int
    __contador: np.array
    def __init__(self,tamaño):
        self.__tamaño = tamaño
        self.__arreglo = np.full((tamaño+2,4),0)
        self.__contador = np.full(tamaño+2,0)

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

    def cuadradoMedio(self, valor):
        valor = valor ** 2
        return self.metodoDiv(valor)

    def Alfanumerio(self,cadena):
        total=0
        for caracter in cadena:
            digito = ord(caracter)
            total += digito
        return self.metodoDiv(total)
    
    def insertar(self,valor):
        indice1 = self.metodoDiv(valor)
        indice2 = self.__contador[indice1]
        if indice2 == 4:
            # Zona de Overflow
            indice1 = self.__tamaño
            self.__arreglo[indice1][indice2] = valor
            self.__contador[indice1] += 1
        else:
            self.__arreglo[indice1][indice2] = valor
            self.__contador[indice1] += 1
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
    tam//=4
    if primo(tam) == False:
        tam = primoProximo(tam)
    hash = HashingB(tam)

    print(hash.getArreglo())
    """hash.insertar(25453,1)
    hash.insertar(81235,1)
    hash.buscar(25453,1)"""