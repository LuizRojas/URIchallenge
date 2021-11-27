from math import *


def maiorABC(lista):
    a = lista[0]
    b = lista[1]
    c = lista[2]
    resultado = int((a + b + abs(a-b)) / 2)

    if resultado > c:
         print(f'{resultado} eh o maior')
    else:
        print(f'{c} eh o maior')


def separar(valores):
    lista1 = []
    for i in valores.split():
        lista1.append(int(i))
    
    return maiorABC(lista1)


def main():
    separar(str(input()))


if __name__ == '__main__':
    main()
