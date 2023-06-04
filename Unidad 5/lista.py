class Nodo:
    __dato = None
    __sigNodo = None
    
    def __init__(self,dat):
        self.__dato = dat
        self.__sigNodo=None

    def  setItem(self,item):
        self.__dato=item
    
    def setSiguiente(self,siguiente):
        self.__sigNodo=siguiente

    def getSiguiente(self):
        return self.__sigNodo

    def getDato(self):
        return self.__dato


class ListaEnlazada:
    __cabeza: Nodo
    
    def __init__(self):
        self.__cabeza = None
    
    def insertar(self, item):
        NuevoNodo = Nodo(item)
        if self.__cabeza == None:
            self.__cabeza = NuevoNodo
        elif not self.nodoRelacionado(item):
                NuevoNodo.setSiguiente(self.__cabeza)
                self.__cabeza = NuevoNodo
    
    def __str__(self) -> str:
        return str(self.__cabeza.getDato())
    
    def nodoRelacionado(self,valor):
        aux = self.__cabeza
        repetido = False
        while aux != None and not repetido:
            if aux.getDato() == valor:
                repetido = True
            aux = aux.getSiguiente()
        return repetido