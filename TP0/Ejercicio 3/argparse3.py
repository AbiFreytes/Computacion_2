# #3- Escribir un programa en Python que acepte argumentos de línea de comando para leer un archivo de texto. 
# #El programa debe contar el número de palabras y líneas del archivo e imprimirlas en la salida estándar. 
# #Además el programa debe aceptar una opción para imprimir la longitud promedio de las palabras del archivo. 
# #Esta última opción no debe ser obligatoria. Si hubiese errores deben guardarse el un archivo cuyo nombre será "errors.log" usando la redirección de la salida de error.

import sys
import argparse
from contextlib import redirect_stderr

def main():
    parser = argparse.ArgumentParser()

    try:
        parser.add_argument('-infile', help='File thats going to be open') #parser.add_argument('-infile', type=argparse.FileType('r'), help='File thats going to be open')
        parser.add_argument('-opt', action='store_true', help='Optional average lenght of words on the chosen file')
        args = parser.parse_args()

        with open(args.infile, 'r') as file:
            lines = file.readlines()
            t_words = 0
            n_lines = len(lines)
            le_words = 0

        for line in lines:
            words_per_line = line.split()
            t_words += len(words_per_line)

        if args.opt:
            le_words = sum(len(word) for word in words_per_line)
            if t_words > 0:
                average = le_words / t_words
                sys.stdout.write(f"La cantidad de lineas del archivo es {n_lines} y la cantidad de palabras en el archivo son {t_words}\n")
                sys.stdout.write(f"La longitud promedio de las palabras en el archivo es {average}")
        else:
            sys.stdout.write(f"La cantidad de lineas del archivo es {n_lines} y la cantidad de palabras en el archivo son {t_words}")
    
    except:
        sys.stdout.write("Ha ocurrido un error")


if __name__ == "__main__":
    with open('errors.log', 'a') as stderr, redirect_stderr(stderr):    
        main()

