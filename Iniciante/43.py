def converte(lista):
    for cont, i in enumerate(lista):
        lista[cont] = int(i)

def verfica_triangulo(a, b, c):
    verifica = {'ladoA': abs(b - c) < a < (b + c),
                'ladoB': abs(a - c) < b < (a + c),
                'ladoC': abs(a - b) < c < (a + b)}
    for cont, i in enumerate(verifica):
        if i:
            cont += 1
        if cont == 3:
            return True
    return False
        
entrada = input().split()
converte(entrada)
a, b, c = entrada[0], entrada[1], entrada[2]
if verfica_triangulo:
    pass
    