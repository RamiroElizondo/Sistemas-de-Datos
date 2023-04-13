import os
class Nodo:
    def __init__(self,valor,fila,columna):
        self.__valor = valor
        self.__fila = fila
        self.__columna = columna
        self.__siguiente = None

    def getSiguiente(self):
        return self.__siguiente
    
    def setSiguiente(self,sig):
        self.__siguiente = sig
    
    def getValor(self):
        return self.__valor

    def getFila(self):
        return self.__fila
    
    def getColumna(self):
        return self.__columna

class Lista: #Lista Enlazada
    __comienzo: Nodo|None
    def __init__(self):
        self.__comienzo = None
        self.__tamaño = 1

    def getComienzo(self):
        return self.__comienzo
    def estaVacia(self):
        return self.__comienzo == None

    def siguiente(self,valor):
        if self.estaVacia():
            print('Lista Vacia')
        else:
            siguiente = None
            nodo = self.__comienzo
            pos = 1
            while nodo != None:
                if pos == valor:
                    siguiente = nodo.getSiguiente()
                nodo = nodo.getSiguiente()
                pos+=1
        return siguiente

    def anterior(self,fila,columna)->Nodo:

        if self.estaVacia():
            print('Esta Vacia')
        else:
            anterior = None
            nodo = self.__comienzo
            bandera = False
            while nodo != None and bandera == False:
                if fila < nodo.getFila():
                    anterior=nodo
                    bandera = True
                elif fila == nodo.getFila():
                    if columna < nodo.getColumna():
                        anterior=nodo
                        bandera = True
                else:
                    aux = nodo
                nodo = nodo.getSiguiente()

            if nodo == None:
                anterior = aux
            return anterior

    def insertar(self,valor,fila,columna):
        nodo = Nodo(valor,fila,columna)
       
        if self.__comienzo == None:
            self.__comienzo = nodo
        else:
            if self.__comienzo.getFila() > fila:
                    nodo.setSiguiente(self.__comienzo)
                    self.__comienzo = nodo
            elif self.__comienzo.getFila() == fila:
                    if self.__comienzo.getColumna() > columna:
                        nodo.setSiguiente(self.__comienzo)
                        self.__comienzo = nodo
            else:
                previo = self.anterior(fila,columna)
                nodo.setSiguiente(previo.getSiguiente())
                previo.setSiguiente(nodo)



    def suprimir(self,valor):
        if self.estaVacia():
            print('Esta Vacia')
        else:
            if self.__comienzo.getValor()== valor:
                self.__comienzo = self.__comienzo.getSiguiente
            else:
                previo = self.anterior(valor)
                sig = self.siguiente(valor)
                previo.setSiguiente(sig)

    def buscar(self,valor):
        bandera = False
        pos = 0
        nodo = self.__comienzo
        while nodo != None and bandera != True:
            if nodo.getValor() == valor:
                print('Encontre el elemento')
                bandera = True
            pos+=1
            nodo = nodo.getSiguiente()
        if bandera ==  False:
            pos = -1
        else:
            pos = pos -1
        return pos
    
    def recorrer(self):
        if self.estaVacia():
            print('Esta Vacia')
        else:
            nodo = self.__comienzo
            while nodo.getSiguiente() != None:
                print('Fila {} Columna {} Valor {}'.format(nodo.getFila(),nodo.getColumna(),nodo.getValor()))
                nodo = nodo.getSiguiente()
        print('Fila {} Columna {} Valor {}'.format(nodo.getFila(),nodo.getColumna(),nodo.getValor()))
        print('\n')

def sumar(matriz1,matriz2):
    matrizR = Lista()
    nodo1 = matriz1.getComienzo()
    nodo2 = matriz2.getComienzo()
    print(nodo1.getFila(),' == ',nodo2.getFila())
    if nodo1.getFila() < nodo2.getFila():
        while nodo1.getSiguiente() != None:
            print('Nodo 1 -',nodo1.getValor(),'Nodo 2 -',nodo2.getValor())
            if nodo1.getFila() == nodo2.getFila() and nodo1.getColumna() == nodo2.getColumna():
                valor = nodo1.getValor() + nodo2.getValor()
                matrizR.insertar(valor,nodo1.getFila(),nodo1.getColumna())
                nodo1 = nodo1.getSiguiente()
            else:
                matrizR.insertar(nodo1.getValor(),nodo1.getFila(),nodo1.getColumna())
                matrizR.insertar(nodo2.getValor(),nodo2.getFila(),nodo2.getColumna())
                nodo1 = nodo1.getSiguiente()
                nodo2 = nodo2.getSiguiente()
    elif nodo1.getFila() == nodo2.getFila():
        if nodo1.getColumna() < nodo2.getColumna():
            while nodo1.getSiguiente() != None:
                print('Nodo 1 -',nodo1.getValor(),'Nodo 2 -',nodo2.getValor())
                if nodo1.getFila() == nodo2.getFila() and nodo1.getColumna() == nodo2.getColumna():
                    valor = nodo1.getValor() + nodo2.getValor()
                    matrizR.insertar(valor,nodo1.getFila(),nodo1.getColumna())
                    nodo1 = nodo1.getSiguiente()
                else:
                    matrizR.insertar(nodo1.getValor(),nodo1.getFila(),nodo1.getColumna())
                    matrizR.insertar(nodo2.getValor(),nodo2.getFila(),nodo2.getColumna())
                    nodo1 = nodo1.getSiguiente()
                    nodo2 = nodo2.getSiguiente()
    return matrizR

if __name__ == '__main__':

    os.system('cls')
    matriz1 = Lista()
    matriz1.insertar(2,4,5)
    matriz1.insertar(10,4,2)
    matriz1.insertar(5,3,2)
    matriz1.insertar(9,1,4)
    matriz1.insertar(20,10,4)
    
    matriz2 = Lista()
    matriz2.insertar(2,4,5)
    matriz2.insertar(10,6,8)
    matriz2.insertar(5,9,2)
    matriz2.insertar(9,8,7)

    matriz1.recorrer()
    matriz2.recorrer()
    matrizR = sumar(matriz1,matriz2)
    matrizR.recorrer()