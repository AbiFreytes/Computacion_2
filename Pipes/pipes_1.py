#1- Escribir un programa en Python que comunique dos procesos. 
# El proceso padre deberá leer un archivo de texto y enviar cada línea del archivo al proceso hijo a través de un pipe. 
# El proceso hijo deberá recibir las líneas del archivo y, por cada una de ellas, contar la cantidad de palabras que contiene y mostrar ese número.

import subprocess
import os

def main():
    parent_pid = os.getpid()
    print(f"PID del padre: {parent_pid}")
    # Abrir un pipe para comunicar el proceso padre con el hijo
    p = subprocess.Popen(['python', '-u', 'child_1.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    child_pid = p.pid
    print(f"PID del hijo: {child_pid}")
    # Leer el archivo de texto y enviar cada línea al proceso hijo
    with open('archivo.txt', 'r') as f:
        for line in f:
            # Enviar la línea al proceso hijo
            p.stdin.write(line.encode('utf-8'))
            p.stdin.flush()
            # Recibir la respuesta del proceso hijo e imprimirlo
            response = p.stdout.readline().decode('utf-8').rstrip()
            print(response)

    # Cerrar el pipe y esperar a que el proceso hijo termine
    p.stdin.close()
    p.wait()

if __name__ == '__main__':
    main()