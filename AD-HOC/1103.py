while True:
    entrada: str = input().split()
    if entrada == ['0', '0', '0', '0']:
        break
    valores = {
        'h1' : int(entrada[0]),  # hora atual
        'm1' : int(entrada[1]),  # minuto atual
        'h2' : int(entrada[2]),  # hora programada
        'm2' : int(entrada[3])   # minuto programado
    }
    total_minutos = ((valores['h2'] * 60) + valores['m2']) - (valores['h1'] * 60) + valores['m1']
    print(total_minutos)
