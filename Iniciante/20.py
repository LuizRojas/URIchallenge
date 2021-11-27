# inserir o valor da entrada
entrada = int(input())
# converter o valor para anos
anos = entrada // 365
meses = anos % 12
dias = meses % 30

print(meses, dias)
# imprimir na tela 
print(
    f'{anos} ano (s)\n{meses} mes (es)\n{dias} dia (s)'
)
