import os
from Menu import Menu

if __name__ == '__main__':
    os.system('cls')
    menu = Menu()
    opcion = None

    while opcion != 'z':
        menu.mostrar()
        opcion = input('Tu opcion: ')
        menu.menuOpciones(opcion)

    print('Saliendo del Programa'.center(30,'-'))