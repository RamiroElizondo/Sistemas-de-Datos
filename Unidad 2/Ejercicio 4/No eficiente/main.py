import os
from ColaEnlazada import Cola
import random


def menor(colas):
    minimo = colas[0].getTamaño()
    indice = 0
    
    for i in range(len(colas)):
        
        if colas[i].getTamaño() < minimo:
            minimo = colas[i].getTamaño()
            indice = i
    
    return indice


if __name__ == '__main__':
    os.system('cls')
    cola1 = Cola()
    cola2 = Cola()
    cola3 = Cola()

    tiempoSimulacion = int(input('Ingrese el tiempo de simulacion: '))
    frecuencia = 2
    acumuladorEsperas = 0
    reloj = 0
    cajeros = [0,0,0] #Cajeros[0] es cajero 1, cajeros[1] es cajero 2, cajeros[2] es cajero 3
    colas = [cola1,cola2,cola3]
    maximos = [0,0,0] #Maximo de cada cola

    entro = None
    atendidos = 0
    acumuladorEsperas = 0
    indice = None
    while reloj != tiempoSimulacion:
        valor = random.random()
        demora = random.randint(1,10)
        print(f'Reloj: {reloj}'.center(50,'-'))
        print('-Cola 1: {} - Cola 2: {} - Cola 3: {}'.format(cola1.getTamaño(),cola2.getTamaño(),cola3.getTamaño()))
        
       
        if valor > 1/frecuencia:
            print('Llego un cliente con demora de: ',demora,' minutos')
            indice = menor(colas) #Retorna el indice de la cola a la que entra
            print('Entro a cola: ',indice+1)
            colas[indice].insertar(demora)
            entro = True
        else:
            entro = False
            print('No llego un cliente')

        if cajeros[0] == 0:
            if not colas[0].estaVacia():
                nodo1 = colas[0].suprimir()
                print('Entre en cajero 1')
                print('Atendiendo cliente en cola 1 con tiempo:', nodo1.getValor())
                acumuladorEsperas += nodo1.getEsperando()
                ejecutando = nodo1.getValor()
                cajeros[0] = 5
                atendidos +=1
                if nodo1.getEsperando() > maximos[0]:
                    maximos[0] = nodo1.getEsperando()
        else:
            cajeros[0] -=1
            ejecutando -=1 
            print('Tiempo restante en cajero 1: ',cajeros[0])
            if entro == True and indice == 0:
                    print('-----------------------------')
                    print('El Cajero 1 esta ocupada, el cliente se suma a la cola 1')

            if nodo1.getValor() > 5:
                if cajeros[0] == 0:
                    print('-----------------------------')
                    print('El cajero 1 llego a su tiempo maximo de atencion')
                    print('El cliente vuelva a la cola para terminar su atencion')
                    print('-----------------------------')
                    colas[0].insertar(nodo1.getValor()-5)
            elif ejecutando == 0:
                print('Se termino de atender al cliente del cajero 1')
                cajeros[0] = 0

        if cajeros[1] ==0  :
            if not colas[1].estaVacia():
                nodo2 = colas[1].suprimir()
                print('Entre en cajero 2')
                print('Atendiendo cliente en cola 2 con tiempo:', nodo2.getValor())
                acumuladorEsperas += nodo2.getEsperando()
                ejecutando = nodo2.getValor()
                cajeros[1] = 3
                atendidos +=1
                if nodo2.getEsperando() > maximos[1]:
                    maximos[1] = nodo2.getEsperando()
        else:
            cajeros[1] -=1
            ejecutando -=1
            print('Tiempo restante en cajero 2: ',cajeros[1])
            if entro == True and indice == 1:
                print('-----------------------------')
                print('El Cajero 2 esta ocupada, el cliente se suma a la cola 2')

            if nodo2.getValor() > 5:
                if cajeros[1]== 0:
                    print('-----------------------------')
                    print('El cajero 2 llego a su tiempo maximo de atencion')
                    print('El cliente vuelva a la cola para terminar su atencion')
                    print('-----------------------------')
                    colas[1].insertar(nodo2.getValor()-5)
            elif ejecutando == 0:
                print('Se termino de atender al cliente del cajero 2')
                cajeros[1] = 0
        
        if cajeros[2] == 0 :
            if not colas[2].estaVacia():
                nodo3 = colas[2].suprimir()
                print('Entre en cajero 3')
                print('Atendiendo cliente en cola 3 con tiempo:', nodo3.getValor())
                acumuladorEsperas += nodo3.getEsperando()
                ejecutando = nodo3.getValor()
                cajeros[2] = 4
                atendidos +=1
                if nodo3.getEsperando() > maximos[2]:
                    maximos[2] = nodo3.getEsperando()
        else:
            cajeros[2] -=1
            ejecutando -=1
            print('Tiempo restante en cajero 3: ',cajeros[2])
            if entro == True and indice == 2:
                print('-----------------------------')
                print('El Cajero 3 esta ocupada, el cliente se suma a la cola 3')

            if nodo3.getValor() > 5:
                if cajeros[2] == 0:
                    print('-----------------------------')
                    print('El cajero 3 llego a su tiempo maximo de atencion')
                    print('El cliente vuelva a la cola para terminar su atencion')
                    print('-----------------------------')
                    colas[2].insertar(nodo3.getValor()-5)
            elif ejecutando == 0:
                print('Se termino de atender al cliente del cajero 3')
                cajeros[2] = 0
        colas[0].aumentarValores()
        colas[1].aumentarValores()
        colas[2].aumentarValores()
        print('- Cola 1: {} - Cola 2: {} - Cola 3: {}'.format(cola1.getTamaño(),cola2.getTamaño(),cola3.getTamaño()))
        reloj +=1
    
    print('\nMaximo Cola 1: {} Maximo Cola 2: {} Maximo Cola 3: {}'.format(maximos[0],maximos[1],maximos[2]))
    print('El tiempo maximo de espera en la Cola 1 fue: ',maximos[0])
    print('El tiempo maximo de espera en la Cola 2 fue: ',maximos[1])
    print('El tiempo maximo de espera en la Cola 3 fue: ',maximos[2])

    print('Cantidad de Clientes atendidos: ',atendidos)

    print('Cantidad de clientes que quedaron sin atender',cola1.getTamaño()+cola2.getTamaño()+cola3.getTamaño())

    print('Promedio de espera de los clientes atendidos: ',acumuladorEsperas/atendidos)

    sumaEsperas = cola1.recorrer()+cola2.recorrer()+cola3.recorrer()
    sumaTamaño = cola1.getTamaño()+cola2.getTamaño()+cola3.getTamaño()
    valor = 0

    if sumaTamaño != 0:
        valor = sumaEsperas / sumaTamaño
    print('Promedio tiempo espera de los clientes sin atender: ',valor)