entrada = int(input())

horas = entrada // 3600
entrada = entrada - (horas * 3600)
minutos = entrada // 60
segundos = minutos % 1

print(f'{horas}:{minutos}:{segundos}')
