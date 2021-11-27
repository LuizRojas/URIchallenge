def separar(valores):
    lista_valores = []
    nova_lista_valores = []

    for i in valores.split():
        lista_valores.append(i)

    for e in lista_valores:
        nova_lista_valores.append(float(e))

    return calcular_areas(nova_lista_valores)


def calcular_areas(lista):
    areas = dict()
    areas['triangulo'] = (lista[0] * lista[2]) / 2
    areas['circulo'] = 3.14159 * (lista[2] ** 2)
    areas['trapezio'] = (lista[0] + lista[1]) * lista[2] / 2
    areas['quadrado'] = lista[1] ** 2
    areas['retangulo'] = lista[0] * lista[1]

    print(f'''TRIANGULO: {areas['triangulo']:.3f}\nCIRCULO: {areas['circulo']:.3f}\nTRAPEZIO: {areas['trapezio']:.3f}\nQUADRADO: {areas['quadrado']:.3f}\nRETANGULO: {areas['retangulo']:.3f}''')


def main():
    separar(str(input()))


if __name__ == '__main__':
    main()
