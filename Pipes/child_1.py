import sys

for line in sys.stdin:
    word_count = len(line.split())
    # Imprimir el número de palabras en la línea
    print(word_count)
    sys.stdout.flush()
