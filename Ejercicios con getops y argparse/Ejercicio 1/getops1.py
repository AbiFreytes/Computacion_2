#1- Escribir un programa en Python que acepte un número de argumento 
#entero positivo n y genere una lista de los n primeros números impares. El programa debe imprimir la lista resultante en la salida estandar.
class NotValidNumber(Exception):
    pass

import sys
import getopt

def main():
    number = ''
    argsv = sys.argv[1:] #el nombre del archivo es el primero que se pasa por lo que tiene indice 0, e iniciamos desde 1
    
    try:
        opts, args = getopt.getopt(argsv, "n:", ["odd_numbers="])
    except getopt.GetoptError as err:
        print(err)
        opts = []

    for opt, arg in opts:
        if opt in ['-n', '--odd_numbers']:
            number = arg
            print(f"Cantidad de numeros impares a encontrar {number}")

    number = int(number)

    if number > 0:
        list = []
        for i in range(1, number*2, 2):
            list.append(i)
    else:
        raise NotValidNumber("Not valid number")
    
    print(list)
    
if __name__ == "__main__":
    main()




