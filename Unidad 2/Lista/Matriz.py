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
                print('Fila Ingresada',fila)
                print('Fila del nodo',nodo.getFila())
                if fila < nodo.getFila():
                    print('Fui Menor')
                    anterior=nodo
                    bandera = True
                elif fila == nodo.getFila():
                    if columna < nodo.getColumna():
                        anterior=nodo
                        bandera = True
                nodo = nodo.getSiguiente()
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

                print('Se inserto correctamente')

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
                print(nodo.getValor())
                nodo = nodo.getSiguiente()
        print(nodo.getValor())

if __name__ == '__main__':
    os.system('cls')
    lista = Lista()
    lista.insertar(2,4,5)
    lista.insertar(10,4,2)
    lista.insertar(5,3,2)
    lista.insertar(9,1,4)
    lista.recorrer()

    