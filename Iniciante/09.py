def vendedor():
    informacoes = dict()

    informacoes['Nome'] = str(input())
    informacoes['Salario fixo'] = float(input())
    informacoes['Vendas'] = float(input())
    
    print(f'TOTAL = R$ {informacoes["Salario fixo"] + informacoes["Vendas"] * 0.15:.2f}')


def main():
    vendedor()


if __name__ == '__main__':
    main()
