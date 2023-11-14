import os

pipe_name = '/tmp/matriz_pipe'


def calcular_elemento(fila, columna):
    resultado = 0
    for i in range(2):
        resultado += matriz1[fila][i] * matriz2[i][columna]
    return resultado


def child(fifo):
    pipeout = os.open(fifo, os.O_WRONLY)
    for fila in range(2):
        for columna in range(2):
            elemento = calcular_elemento(fila, columna)
            mensaje = f'{fila},{columna}:{elemento}\n'
            os.write(pipeout, mensaje.encode())


def parent(fifo):
    pipein = open(fifo, 'r')
    resultados = [[0, 0], [0, 0]]

    for _ in range(4):
        mensaje = pipein.readline().strip()
        fila, columna = map(int, mensaje.split(':')[0].split(','))
        resultado = int(mensaje.split(':')[1])
        resultados[fila][columna] = resultado

    print("Matriz Resultante:")
    for fila in resultados:
        print(fila)


if not os.path.exists(pipe_name):
    os.mkfifo(pipe_name)

matriz1 = [[1, 2], [3, 4]]
matriz2 = [[5, 6], [7, 8]]

pid = os.fork()

if pid != 0:
    parent(pipe_name)
else:
    child(pipe_name)