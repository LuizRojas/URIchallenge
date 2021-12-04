# ler o valor inteiro
numero = int(input())
print(numero)

lista = (100, 50, 20, 10, 5, 2, 1)

# dividir o maximo possivel para cada nota na lista
for nota in lista:
    valor = int(numero / nota)
    numero = numero - (valor * nota)

    print(f'{valor} nota(s) de R$ {nota},00')
