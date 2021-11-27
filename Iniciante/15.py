from math import *


def separar(pontoA, pontoB):
    lista1 = list()
    lista2 = list()

    for i in pontoA.split():
        lista1.append(float(i))
    for e in pontoB.split():
        lista2.append(float(e))
    
    return distancia(lista1, lista2)


def distancia(lista1, lista2):
    x1 = lista1[0]
    y1 = lista1[1]
    x2 = lista2[0]
    y2 = lista2[1]
    dist = sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))
    
    print(f'{dist:.4f}')


def main():
    xy1 = input()
    xy2 = input()
    separar(xy1, xy2)


if __name__ == '__main__':
    main()
