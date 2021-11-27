from math import trunc


def etapa_1():
    caracteres = []
    palavra = str(input())
    for i in palavra:
        if i.isalpha():
            caracteres.append(ord(i) + 3)
        else:
            caracteres.append(ord(i))
    return caracteres


def etapa_3(lista):
    etapa_3 = []
    for e in lista:
        if e in lista[trunc((len(lista) + 1) / 2):]:
            etapa_3.append(chr(e - 1))
        else:
            etapa_3.append(chr(e))
    unir = ''.join(etapa_3)
    return unir


n_termos = int(input())
for i in range(n_termos):  
    etapa_2 = etapa_1()[::-1]
    print(etapa_2)
    print(etapa_3(etapa_2))

# INCOMPLETO
