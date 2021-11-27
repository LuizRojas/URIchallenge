def converter(compra1, compra2):
    valores1 = []
    valores2 = []
    for i in compra1:
        valores1.append(float(i))
    for e in compra2:
        valores2.append(float(e))

    return somar_valores(valores1, valores2)
    

def somar_valores(compra1, compra2):
    valor1 = compra1[1] * compra1[2]
    valor2 = compra2[1] * compra2[2]
    soma = valor1 + valor2
    print(f'VALOR A PAGAR: R$ {soma:.2f}')


def main():
    carrinho1 = str(input()).split()
    carrinho2 = str(input()).split()
    converter(carrinho1, carrinho2)


if __name__ == '__main__':
    main()
