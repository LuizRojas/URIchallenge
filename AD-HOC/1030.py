entrada = int(input())
casos = []
for i in range(entrada):
    valores = input().split()
    pessoas = int(valores[0])
    salto = int(valores[1])
    casos.append([pessoas, salto])

print(casos)
for caso in casos:
    for ciclo in range(0, caso[0], caso[1]):
        caso.pop(ciclo)
        print(caso)
