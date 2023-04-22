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

class ListaEContenido:
    def __init__(self):
        self.__cabeza = None
        self.__tamaño = 0
    
    def estaVacia(self):
        return self.__cabeza == None
    
    def anterior(self,valor):
        if self.estaVacia(): # Por si llamo a esta funcion fuera del insertar
            print('Esta vacia') 
        else:
            anterior = None
            nodo = self.__cabeza
            
            while nodo != None and valor > nodo.getValor():
                anterior = nodo
                nodo = nodo.getSiguiente()
            return anterior

    def siguiente(self,valor):
        if self.estaVacia():
            print('Esta vacia') 
        else:
            siguiente = None
            nodo = self.__cabeza
            bandera = False
            while nodo != None and bandera == False:
                if nodo.getValor() == valor:
                    siguiente = nodo.getSiguiente()
                    bandera = True
                nodo = nodo.getSiguiente()
            if nodo == None:
                print('No hay siguiente')
                return None
            else:
                return siguiente

    def insertar(self,valor):
        nodo = Nodo(valor) #creo la componente de la lista
        if self.estaVacia():
            self.__cabeza=nodo
        else:
            if self.__cabeza.getValor() > valor:
                nodo.setSiguiente(self.__cabeza)
                self.__cabeza = nodo
            else:
                previo = self.anterior(valor)
                nodo.setSiguiente(previo.getSiguiente())
                previo.setSiguiente(nodo)
            self.__tamaño+=1
    def suprimir(self,valor):
        if self.estaVacia():
            self.__cabeza=nodo
        else:
            anterior = self.anterior(valor)
            siguiente = self.siguiente(valor)
            anterior.setSiguiente(siguiente)
            self.__tamaño-=1

    def recorrer(self):
        if self.estaVacia(): 
            print('Esta vacia') 
        else:
            nodo = self.__cabeza
            while nodo != None:
                print(nodo.getValor())
                nodo = nodo.getSiguiente()
    
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
    lista = ListaEContenido()
    lista.insertar(7)
    lista.insertar(6)
    lista.insertar(10)
    lista.insertar(50)
    lista.insertar(20)
    lista.recorrer()
    print('\n')
    """nodo = lista.siguiente(50)
    if nodo != None:
        print(nodo.getValor())"""
    lista.suprimir(10)
    lista.recorrer()
    primero = lista.primerElemento()
    print('Primer nodo: ',primero.getValor())
    ultimo = lista.ultimoElemento()
    print('Ultimo nodo: ',ultimo.getValor())
