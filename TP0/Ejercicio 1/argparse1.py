#1- Escribir un programa en Python que acepte un número de argumento 
#entero positivo n y genere una lista de los n primeros números impares. El programa debe imprimir la lista resultante en la salida estandar.

class NotValidNumber(Exception):
    pass

import argparse

def main():
    parser = argparse.ArgumentParser(description='Generador de lista de numeros impares')
    parser.add_argument('-n', help='Cantidad de numeros impares que debe haber en la lista')
    args = parser.parse_args()

    if int(args.n) > 0:
        list = []
        for i in range(1, int(args.n)*2, 2):
            list.append(i)
    else:
        raise NotValidNumber("Not valid number")
    
    print(list)

if __name__ == "__main__":
    main()

