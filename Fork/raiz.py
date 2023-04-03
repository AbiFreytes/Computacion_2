import numpy
import argparse
import os
import sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n','--number',type=float, help='radicand')
    parser.add_argument('-f','--fork',help='fork process', action='store_true')
    args = parser.parse_args()
    
    if args.number<0:
        raise ValueError('Ingresar un número no negativo')
    if args.fork == True:
        ret = os.fork()
        if ret > 0:
            raiz = numpy.sqrt(args.number)
            sys.stdout.write(str(raiz))
        elif ret == 0:
            if args.number == 0.0:
                sys.stdout.write('\n0.0')
            else:
                raiz = numpy.sqrt(args.number)
                sys.stdout.write(f'\n-{raiz}')
    else:
        sys.stdout.write(f'Seleccionaste el número: {args.number}')

if __name__ == '__main__':
    main()
