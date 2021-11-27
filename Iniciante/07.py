valores = []
for i in range(4):
    valores.append(int(input()))
AB = valores[0] * valores[1]
CD = valores[2] * valores[3]
dif = AB - CD
print(f'DIFERENCA = {dif}')
