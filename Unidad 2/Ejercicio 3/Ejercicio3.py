import os
import random
from Cola_Enlazada2 import Cola

if __name__ == '__main__':
    os.system('cls')
    cola = Cola()
    
    tiempoSimulacion = int(input('Ingrese el tiempo maximo de la simulacion: '))
    frecuencia = 5 #Frecuencia en la que llegan los trabajos
    acumuladorEsperas:int = 0
    
    ocupado = 0 #0 no esta impriminedo 1 si 
    atendidos:int = 0
    reloj = 0
    entro = None

    while reloj != tiempoSimulacion:
        valor = random.random() #Numero aleatoria que utilizamos para indicar si llega o no un trabajo en cada minuto
        print(f'Reloj: {reloj}'.center(20,'-'))
       
        demora = random.randint(1, 10) #Trabajo
        
        if valor < 1/frecuencia: #Llego un trabajo
            print('Llego un trabajo')
            cola.insertar(demora)
            entro = True
        else:
            entro = False
            print('No llego ningun trabajo')
        if ocupado == 0: # Si impresora esta ocupada o no

            if not cola.estaVacia():
                nodo = cola.suprimir()
        
                print('Imprimiendo el trabajo que tarda ',nodo.getValor())
                acumuladorEsperas += nodo.getEspernado() #Sumar el valor que espero
                atendidos += 1
                ocupado = 5
                ejecutando= nodo.getValor()
                    
        else:
            ejecutando -=1
            ocupado -= 1
            print(ocupado)
            if entro == True:
                print('-----------------------------')
                print('La impresora esta ocupada, el trabajo se agrego a la cola')

            if nodo.getValor() > 5:
                if ocupado == 0:
                    print('-----------------------------')
                    print('La impresora llego al tiempo limite de trabajo')
                    print('El trabajo vuelve a la cola para luego terminar su impresion')
                    print('-----------------------------')
                    cola.insertar(nodo.getValor()-5)
            elif ejecutando == 0:
                print('El trabajo se termino de imprimir')
                ocupado = 0

        cola.aumentarValores()
        reloj += 1


    print('Trabajos que quedaron sin Atender: ')
    cola.mostrar()
    print('Trabajos atendidos: ',atendidos)
    
    print(acumuladorEsperas)
    promedio = acumuladorEsperas / atendidos
    print('El promedio de espera es de: ',promedio)
