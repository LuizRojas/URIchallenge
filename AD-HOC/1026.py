lista = []
for i in range(2):
    lista.append(input().split())

for valor in lista:
    if int(valor[0]) > int(valor[1]):
        print(int(valor[0]) - int(valor[1]))
    else:
        print(int(valor[1]) - int(valor[0]))
