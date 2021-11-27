'''import numpy as np

entrada = int(input())

for i in range(entrada):
    valores = input().split()
    print(np.gcd(int(valores[0]), int(valores[1])))'''

'''Descobrindo o MDC entre valores com resursão'''

def mdc(x, y):
    if (y == 0):
        return x
    else:
        return mdc(y, x % y)

n = int(input())

for i in range(n):
    valores = input().split()
    p1 = int(valores[0])
    p2 = int(valores[1])
    print(mdc(p1, p2))
