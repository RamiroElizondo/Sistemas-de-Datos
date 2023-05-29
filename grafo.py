"""
Ejercicio 1
Definir el T.A.D Grafo/Digrafo:
a) Especificación.
b) Representación (para la representación secuencial de grafo, utilizar arreglo unidimensional)
c) Implementación de todas las operaciones.
"""
from cola import Cola
from pila import Pila

class Grafo:
    __arreglo = [[0,1,1,0,0,0],[1,0,0,0,0,0],[0,0,1,0,0,1],[1,0,0,0,1,0],[0,0,1,0,1,1],[1,0,1,0,0,1]]

    def mostrar(self):
        for i in range(6):
            for j in range(6):
                print(self.__arreglo[i][j],end=' ')
            print('\n')

    def __posVertice(self,vertice,vertices):
        for i in range(len(vertices)):
            if vertices[i] == vertice:
                return i
        raise Exception("Vertice inexistente")

    def adyacentes(self,vertice,vertices):
        pos = self.__posVertice(vertice,vertices)
        ady = []
        for i in range(len(vertices)):
            if self.__arreglo[pos][i]:
                ady.append(vertices[i])
        return ady
    

    def REA(self,inicio):
        visitados = [False] *len(self.__arreglo)
        cola = Cola()
        cola.insertar(inicio)
        visitados.append(inicio)

        while not cola.estaVacia():
            verticeActual = cola.suprimir().getValor()
            print(verticeActual+1)

            for vecino in self.__arreglo[verticeActual]:
                if not visitados[vecino]:
                    visitados[vecino] = True
                    cola.insertar(vecino)
    def busquedaProfundidad(self,vertice,vertices):
        visitados = []
        pila = []
        pila.append(vertice)
        while len(pila) > 0:
            v = pila.pop()
            if v not in visitados:
                visitados.append(v)
                ady = self.adyacentes(v,vertices)
                for w in ady:
                    pila.append(w)
        return visitados
    def REP(self,inicio):
        visitados = []
        pila = Pila()
        pila.insertar(inicio)
        while not pila.esta_vacia():
            verticeActual = pila.suprimir().getValor()
            print(verticeActual)

            for vecino in reversed(self.__arreglo[verticeActual]):
                if vecino not in visitados:
                    pila.insertar(vecino)

if __name__ == '__main__':
    grafo = Grafo()
    vertices = [1,2,3,4,5,6]
    grafo.mostrar()
    #vertice = int(input('Ingrese un Vertice: '))
    #grafo.adyacente(vertice-1)
    vertice = 1
    lista = grafo.busquedaProfundidad(vertice,vertices)
    print('Desde el nodo 1: ',lista)
