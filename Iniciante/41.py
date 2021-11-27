entrada = input().split()
x, y = float(entrada[0]), float(entrada[1])
cord = {
    'Q1': (x >= 0 and y >= 0),
    'Q2': (x <= 0 and y >= 0),
    'Q3': (x <= 0 and y <= 0),
    'Q4': (x >= 0 and y <= 0),
    'Origem': (x == 0 and y == 0)
}
for key, valores in cord.items():
    if valores:
        print(f'{key}')
        break
