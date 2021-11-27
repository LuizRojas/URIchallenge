def converte(lista):
    for cont, i in enumerate(lista):
        lista[cont] = int(i)

entrada = input().split()
converte(entrada)
copia = entrada.copy()
copia.sort()

for contagem, i in enumerate(copia, start=1):
    print(i)
    if contagem == len(entrada):
        print()
for i in entrada:
    print(i)
