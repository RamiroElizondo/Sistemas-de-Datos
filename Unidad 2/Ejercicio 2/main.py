import os
from Pila import Pila

def obtenerPilas(pila1,pila2,pila3):
    arreglo1= pila1.getElementos()
    arreglo2= pila2.getElementos()
    arreglo3= pila3.getElementos()
    pilas = [arreglo1,arreglo2,arreglo3]
    return pilas

def mostrarPilas(arreglos,cantidad):
    for i in range(cantidad-1,-1,-1):
        print('\t{}|{}\t \t{}|{}\t \t{}|{}\t'.format(
            arreglos[0][i],arreglos[0][i],
            arreglos[1][i],arreglos[1][i],
            arreglos[2][i],arreglos[2][i]))
        
def termino(pila3,cantidadDiscos):

    return pila3.getTope() == cantidadDiscos

if __name__ == '__main__':
    
    cantidad = int(input('Ingrese la cantidad de discos: '))
    pila1 = Pila(cantidad)
    pila2 = Pila(cantidad)
    pila3 = Pila(cantidad)
    
    for i in range(cantidad,0,-1):  #Inicializamos la primer pila con 1,2,3
        pila1.insertar(i)

    print('Comienza el juego'.center(27,'-'))
    arreglos = obtenerPilas(pila1,pila2,pila3) #Obtenemos los arreglos de numeros de cada pila para facilitar el trabajo
    mostrarPilas(arreglos,cantidad)
    
    pilas=[pila1,pila2,pila3] 
    contador = 0
    while not termino(pila3,cantidad):
        desde = int(input('Desde: '))
        hacia = int(input('Hacia: '))
        indice1 = pilas[desde-1].getTope()
        indice2= pilas[hacia-1].getTope()
        
        if pilas[hacia-1].esta_vacia() == True:
            disco = pilas[desde-1].suprimir()
            pilas[hacia-1].insertar(disco)

            arreglos = obtenerPilas(pila1,pila2,pila3)
            mostrarPilas(arreglos,cantidad)

        elif arreglos[desde-1][indice1-1] < arreglos[hacia-1][indice2-1] :
            disco = pilas[desde-1].suprimir()
            pilas[hacia-1].insertar(disco)

            arreglos = obtenerPilas(pila1,pila2,pila3)
            mostrarPilas(arreglos,cantidad)
        else:
            print('Movimiento no Valido'.center(28,'-'))
            print('No se puede colar un disco grande sobre un disco chico')
        contador+=1
    
    print('Termina el Juego'.center(27,'-'))
    print('Movimientos Realizados',contador)
    print('Movimientos Optimos',2**cantidad-1)
