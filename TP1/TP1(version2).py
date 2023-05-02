import argparse
import os
import sys

def reverse_string(string):
    return string[::-1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", required=True, help="Archivo de texto a procesar")
    args = parser.parse_args()

    filename = args.file

    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        sys.stdout.write(f"Error: el archivo {filename} no se encuentra")
        exit(1)

    pipes = []
    for i in range(len(lines)):
        #Hacemos un pipe y un hijo por cada linea en el archivo
        r, w = os.pipe()
        pid = os.fork()
        if pid == 0:
            #Procesos hijos
            os.close(r)
            line = lines[i].strip()
            inverted_line = reverse_string(line)
            os.write(w, inverted_line.encode()) #encode lo pasa a bytes y decode a string
            os.close(w)
            exit(0)
        else:
            #Proceso del padre
            os.close(w)
            pipes.append(r) #extremo de lectura

    inverted_lines = []
    for pipe in pipes:
        inverted_line = os.read(pipe, 1024).decode().strip() #1024 es el tamaño max del buffer y utilizo el strip para eliminar cualquier espacio en blanco q quede despues de la cadena
        inverted_lines.append(inverted_line + "\n")

    sys.stdout.write("".join(inverted_lines))

    os.wait() 

if __name__ == '__main__':
    main()