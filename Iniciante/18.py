# ler o valor inteiro
entrada = int(input())

# dividir o maximo possivel para notas de 100
notas100 = entrada//100

# definir uma lista com a quantidade de notas:
total_notas = [notas100]

notas = (50, 20, 10, 5, 2, 1)

# e definir o resto de divisao
resto = notas100 % 100
# agora que temos o valor para dividirmos todos os termos, faremos com o restante dos valores
for i in notas:
    nota = resto // i
    resto %= i
    total_notas.append(nota)

print(total_notas)
