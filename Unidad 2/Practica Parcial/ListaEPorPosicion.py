class Nodo:
    def __init__(self,valor):
        self.__valor = valor
        self.__siguiente = None

    def getValor(self):
        return self.__valor

    def getSiguiente(self):
        return self.__siguiente
    
    def setSiguiente(self,sig):
        self.__siguiente = sig

class ListaEPosicion:
    def __init__(self):
        self.__comienzo = None
        self.__tamaño = 1
    
    def estaVacia(self):
        return self.__comienzo == None

    def anterior(self,posicion):
        if self.estaVacia():
            print('Esta Vacia')
        else:
            nodo = self.__comienzo
            bandera = False
            pos=1
            while nodo != None and bandera ==False:
                if pos == posicion-1:
                    anterior=nodo
                    bandera = True
                pos+=1
                nodo = nodo.getSiguiente()
            return anterior
    
    def siguiente(self,posicion):
        if self.estaVacia():
            print('Esta vacia') 
        else:
            siguiente = None
            nodo = self.__comienzo
            bandera = False
            pos = 1
            while nodo != None and bandera == False:
                if posicion == pos:
                    siguiente = nodo.getSiguiente()
                    bandera = True
                pos+=1
                nodo = nodo.getSiguiente()
            if nodo == None:
                print('No hay siguiente')
                return None
            else:
                return siguiente

    def insertar(self,valor,posicion):
        nodo = Nodo(valor)
        if posicion > self.__tamaño:
            raise('Fuera de Rango')
        else:
            if posicion == 1:
                nodo.setSiguiente(self.__comienzo)
                self.__comienzo = nodo
            else:
                previo = self.anterior(posicion)
                nodo.setSiguiente(previo.getSiguiente())
                previo.setSiguiente(nodo)
            self.__tamaño +=1

    def recorrer(self):
        if self.estaVacia():
            print('Esta Vacia')
        else:
            nodo = self.__comienzo
            while nodo != None:
                print(nodo.getValor())
                nodo = nodo.getSiguiente()
    
    def buscarP(self,posicion):
        if posicion > self.__tamaño or self.estaVacia():
            raise 'Fuero de Rango'
            
        if posicion == 1:
            print(self.__comienzo.getValor())
        else:
            nodo = self.anterior(posicion)
            return nodo

    def buscarC(self,contenido):
        if self.estaVacia():
            print('Esta Vacia')
        else:
            nodo = self.__comienzo
            bandera = False
            posicion = 1
            while nodo != None and bandera != True:
                if contenido == nodo.getValor():
                    bandera = True
                    valor = posicion
                nodo = nodo.getSiguiente()
                posicion += 1
            return valor

    def primerElemento(self):
        if self.estaVacia():
            print('Esta Vacia')
        else:
            return self.__cabeza
    
    def ultimoElemento(self):
        if self.estaVacia():
            print('Esta Vacia')
        else:
            nodo = self.__cabeza
            ultimo = None
            while nodo != None:
                if nodo.getSiguiente() == None:
                    ultimo = nodo
                nodo = nodo.getSiguiente()
            return ultimo

if __name__ == '__main__':
    lista = ListaEPosicion()
    lista.insertar(6,1)
    lista.insertar(7,1)
    lista.insertar(10,2)
    lista.insertar(20,4)
    lista.insertar(50,4)
    lista.recorrer()
    print('\n')
    """pos = int(input('Ingrese posicion a buscar: '))
    nodo1 = lista.buscarP(pos)
    print(nodo1.getSiguiente().getValor())

    valor = int(input('Ingrese el valor a buscar: '))
    posicion = lista.buscarC(valor)
    print('Se encuentra en la posicion: ',posicion)"""

    
    nodo = lista.siguiente(3)
    if nodo != None:
        print(nodo.getValor())