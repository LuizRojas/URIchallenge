# ler o valor inteiro
entrada = int(input())

# dividir o maximo possivel para notas de 100
cem = int(entrada / 100)
entrada = entrada - (cem * 100)

# dividir o maximo possivel para notas de 50

# definir uma lista com a quantidade de notas:
notas = (50, 20, 10, 5, 2, 1)

# e definir o resto de divisao
resto = (entrada % 100) % 50
# agora que temos o valor para dividirmos todos os termos, faremos com o restante dos valores
print(f'Notas de 100: {cem}\nNotas de 50: {resto}')
