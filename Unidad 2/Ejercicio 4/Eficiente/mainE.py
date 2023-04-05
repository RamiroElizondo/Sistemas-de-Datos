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

def acccion(cajero,indice,atendidos,acumuladorEsperas,maximo,cola):
    if cajero == 0:
        if not cola.estaVacia():
            nodo = cola.suprimir()
            acumuladorEsperas += nodo.getEsperando()
            ejecutando = nodo.getValor()
            cajero = 5
            atendidos +=1
            
            if nodo.getEsperando() < maximo:
                maximo = nodo.getEsperando()
            
    else:
        cajero -=1
        ejecutando -=1

        
        if entro == True:
            print('-----------------------------')
            print('El Cajero {} esta ocupada, el cliente se suma a la cola {}'.format(indice+1,indice+1))

        if nodo.getValor() > 5:
            if ocupado == 0:
                print('-----------------------------')
                print('El cajero llego a su tiempo maximo de atencion')
                print('El cliente vuelva a la cola para terminar su atencion')
                print('-----------------------------')
                cola.insertar(nodo.getValor()-5)
        elif ejecutando == 0:
            print('Se termino de atender al cliente')
            ocupado = 0

    return (cajero,atendidos,acumuladorEsperas,maximos)


if __name__ == '__main__':
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

    entre = None
    atendidos = 0
    acumuladorEsperas = 0

    while reloj != tiempoSimulacion:
        vallor = random.random()
        demora = random.randint(1,10)
        

        if valor > 1/frecuencia:
            print('Llego un cliente')
            indice = menor(colas) #Retorna el indice de la cola a la que entra
            cola[indice].insertar(demora)
            entre = True
        else:
            entre = False
            print('No llego un cliente')
        
        if indice == 0:
            #cajero,indice,atendidos,acumuladorEsperas,maximo,cola)
            cajeros[0],atendidos,acumuladorEsperas,maximos = accion(cajeros[0],indice,atendidos,acumuladorEsperas,maximos[0],colas[0])
        elif indice == 1:
            cajeros[1],atendidos,acumuladorEsperas,maximos = accion(cajeros[1],indice,atendidos,acumuladorEsperas,maximos[1],colas[1])
        elif indice == 2:
            cajeros[2],atendidos,acumuladorEsperas,maximos = accion(cajeros[2],indice,atendidos,acumuladorEsperas,maximos[2],colas[2])
        reloj +=1
    
    print('Maximo Cola 1: {} Maximo Cola 2: {} Maximo Cola 3: {}'.format(maximos[0],maximos[1],maximos[2]))
    print('El tiempo maximo de espera en la Cola 1 fue: ',maximos[0])
    print('El tiempo maximo de espera en la Cola 2 fue: ',maximos[1])
    print('El tiempo maximo de espera en la Cola 3 fue: ',maximos[2])

    print('Cantidad de Clientes atendidos: ',atendidos)

    print('Cantidad de cleitnes que quedaron sin atender',cola1.getTamaño()+cola2.getTamaño()+cola3.getTamaño())

    print('Promedio de espera de lso clientes atendidos: ',acumuladorEsperas/atendidos)


    valor = cola1.recorrer()+cola2.recorrer()+cola3.recorrer()
    valor = valor / (cola1.getTamaño()+cola2.getTamaño()+cola3.getTamaño())
    print('Promedio tiempo espera de los clientes sin atender: ',valor)
