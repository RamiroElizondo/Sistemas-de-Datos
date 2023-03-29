import random
from Cola_Enlazada import Cola

if __name__ == '__main__':
    cola = Cola()
    
    tiempoSimulacion = input('Ingrese el tiempo maximo de la simulacion: ')
    frecuencia = 5 #Frecuencia en la que llegan los trabajos
    tiempoTrabajo = 5 #Lo maximo que imprime
    tiempoEspera = 0
    tiempoEncurso = 0 #Tiempo que lleva en trabajo la impresora
    ocupado = 0 #0 no esta impriminedo 1 si 
    atendidos= 0

    numeroTrabajo=1
    estimacion= 1/frecuencia
    reloj = 0

    while reloj != tiempoSimulacion:
        valor = random.random() #Numero aleatoria que utilizamos para indicar si llega o no un trabajo en cada minuto
        demora = random.randint(1, 10) #Trabajo
        if valor > estimacion: #Llego un trabajo
            print('Llego un trabajo')
            cola.insertar(demora,numeroTrabajo)
            numeroTrabajo+=1
        if ocupado == 0: # Si impresora esta ocupada o no
            if not cola.estaVacia():
                nodo = cola.suprimir()
                print('Imprimiendo el trabajo que tarda ',nodo.getValor())

                tiempoEspera += nodo.getEspernado() #Sumar el valor que espero
                atendidos += 1
                ocupado = 1
        else:
            print(reloj)
            print('Entro')
            cola.aumentarValores()
            tiempoEncurso+=1
            if tiempoEncurso > tiempoTrabajo:
                ocupado = 0
                print('-----------------------------')
                print('La impresora llego al tiempo limite de trabajo')
                print('El trabajo vuelve a la cola para lugar terminar su impresion')
                print('-----------------------------')
            if demora <= tiempoTrabajo:
                print()
        nodo.setEsperando(esperando-1)
        if nodo.getEspernado() == 0:
            print('El trabajo {} se termino de imprimir'.format(nodo.getNumero()))
            ocupado = 0
            tiempoEncurso = 0
        reloj += 1

    print('Trabajos que quedaron sin Atender: ')
    cola.mostrar()
    promedio = tiempoEspera / atendidos
    print('El promedio de espera es de: ',promedio)
