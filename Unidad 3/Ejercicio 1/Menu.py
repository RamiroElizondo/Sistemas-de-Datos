from ArbolBB import ArbolBB
class Menu:
    __arbol: ArbolBB()

    def __init__(self):
        self.__arbol = ArbolBB()
    
    def mostrar(self):
        print('Menu Cuaderno'.center(40, '-'))
        print('\ta- Ingresar un nodo\n'
            '\tb- Suprimir un nodo\n'
            '\tc- Buscar un nodo\n'
            '\td- Nivel de un nodo\n'
            '\te- Saber si un nodo es hoja\n'
            '\tf- Saber si un nodo es hijo de otro\n'
            '\tg- Saber su un nodo es padre de otro\n'
            '\th- Camino de nodo a otro\n'
            '\ti- Altura del albol\n'
            '\tj- Mostar inOrden\n'
            '\tk- Mostar preOrden\n'
            '\tl- Mostar postOrden\n')
    
    def opcionA(self):
        self.__arbol.insertar(12)
        self.__arbol.insertar(7)
        self.__arbol.insertar(16)
        self.__arbol.insertar(3)
        self.__arbol.insertar(9)
        self.__arbol.insertar(14)
        self.__arbol.insertar(13)
       
        print('Se ingresaron los nodos'.center(30,'-'))

    def opcionB(self):
        valor = int(input('Ingrese el valor del nodo que quiere eliminar: '))
        self.__arbol.suprimir(valor)
        self.opcionJ()
        print(self.__arbol.getRaiz().getValor())
    
    def opcionC(self):
        contenido = int(input('Ingrese el valor del nodo a buscar: '))
        nodo = self.__arbol.buscar(contenido,self.__arbol.getRaiz())
        if nodo!= None:
            print('El elemento esta en el arbol')
            print(nodo.getValor())
        else:
            print('El elemento no esta en el arbol')

    def opcionD(self):
        contenido = int(input('Ingrese el valor del nodo a saber el nivel: '))
        nodo = self.__arbol.buscar(contenido,self.__arbol.getRaiz())
        if nodo != None:
            contador = self.__arbol.nivel(nodo,self.__arbol.getRaiz(),1)
            print('Esta en el nivel: ',contador)
        else:
            print('El elemento no esta en el arbol')
        
    def opcionE(self):
        valor = int(input('Ingrese el valor del nodo a saber si es hoja: '))
        nodo = self.__arbol.buscar(valor,self.__arbol.getRaiz())
        if nodo !=None:
            valor = self.__arbol.hoja(nodo)
            if valor is True:
                print('Es hoja')
            else:
                print('No es hoja')

    def opcionF(self):
        hijo = int(input('Ingrese el valor del hijo: '))
        padre = int(input('Ingrese el valor del padre: '))

        hijo = self.__arbol.buscar(hijo,self.__arbol.getRaiz())
        padre = self.__arbol.buscar(padre,self.__arbol.getRaiz())
        valor = self.__arbol.hijo(hijo,padre)
        if valor is True:
            print('Es hijo')
        else:
            print('No es hijo')

    def opcionG(self):
        padre = int(input('Ingrese el valor del padre: '))
        hijo = int(input('Ingrese el valor del hijo: '))

        hijo = self.__arbol.buscar(hijo,self.__arbol.getRaiz())
        padre = self.__arbol.buscar(padre,self.__arbol.getRaiz())
        valor = self.__arbol.padre(hijo,padre)
        if valor is True:
            print('Es Padre')
        else:
            print('No es Padre')

    def opcionH(self):
        arreglo = [] * 10
        desde = int(input('Ingrese el valor del nodo desde: '))
        hasta = int(input('Ingrese el valor del nodo hasta: '))

        desde = self.__arbol.buscar(desde,self.__arbol.getRaiz())
        hasta = self.__arbol.buscar(hasta,self.__arbol.getRaiz())
        if self.__arbol.hijo(desde, hasta):
            arreglo = self.__arbol.camino(desde,hasta,arreglo)
            print(arreglo)
        else:
            print('No se puede hacer el camino')

    def opcionI(self):
        contador = self.__arbol.altura(self.__arbol.getRaiz())
        print('Altura:',contador)

    def opcionJ(self):
        self.__arbol.inOrden(self.__arbol.getRaiz())
        print('\n')

    def opcionK(self):
        self.__arbol.preOrden(self.__arbol.getRaiz())
        print('\n')

    def opcionL(self):
        
        self.__arbol.postOrden(self.__arbol.getRaiz())
        print('\n')

    def menuOpciones(self,opcion):
        if opcion == 'a':
            self.opcionA()
        elif opcion == 'b':
            self.opcionB()
        elif opcion == 'c':
            self.opcionC()
        elif opcion == 'd':
            self.opcionD()
        elif opcion == 'e':
            self.opcionE()
        elif opcion == 'f':
            self.opcionF()
        elif opcion == 'g':
            self.opcionG()
        elif opcion == 'h':
            self.opcionH()
        elif opcion == 'i':
            self.opcionI()
        elif opcion == 'j':
            self.opcionJ()
        elif opcion == 'k':
            self.opcionK()
        elif opcion == 'l':
            self.opcionL()
        else:
            print('Opcion no valida'.center(30, '-'))
