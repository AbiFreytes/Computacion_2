### Requerimientos
# Escriba un programa que abra un archvo de texto pasado por argumento utilizando el modificador -f.
# * El programa deberá generar tantos procesos hijos como líneas tenga el archivo de texto.
# * El programa deberá enviarle, vía pipes (os.pipe()), cada línea del archivo a un hijo.
# * Cada hijo deberá invertir el orden de las letras de la línea recibida, y se lo enviará al proceso padre nuevamente, también usando os.pipe().
# * El proceso padre deberá esperar a que terminen todos los hijos, y mostrará por pantalla las líneas invertidas que recibió por pipe.
# * Debe manejar los errores.
# ​

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
        r, w = os.pipe()
        pid = os.fork()
        if pid == 0:
            #Procesos hijos
            os.close(r)
            line = lines[i].strip()
            inverted_line = reverse_string(line)
            pid_str = str(os.getpid())
            os.write(w, (pid_str + "|" + inverted_line + "\n").encode())
            os.close(w)
            exit(0)
        else:
            #Proceso del padre
            os.close(w)
            pipes.append(r)

    for pipe in pipes:
        data = os.read(pipe, 1024).decode().strip()
        pid_str, inverted_line = data.split("|")
        sys.stdout.write(f"[PID {pid_str}] {inverted_line}\n")

    os.wait() 

if __name__ == '__main__':
    main()