from math import pow, sqrt

entrada = input().split()
a = float(entrada[0])
b = float(entrada[1])
c = float(entrada[2])

delta = pow(b, 2) - (4 * a * c)

if delta > 0 and a > 0:
    delta = sqrt(delta)
    x1 = (-b + delta) / (2 * a)
    x2 = (-b - delta) / (2 * a)
    print(
        f'R1 = {x1:.5f}\nR2 = {x2:.5f}'
    )

else:
    print('Impossivel calcular')


