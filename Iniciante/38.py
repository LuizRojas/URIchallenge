lanches = {
    '1' : ('Cachorro Quente', 4.00),
    '2' : ('X-Salada', 4.50),
    '3' : ('X-Bacon', 5.00),
    '4' : ('Torrada simples', 2.00),
    '5' : ('Refrigerante', 1.50)
}
pedido = input().split()
lanche = lanches[pedido[0]][1]
qtd = int(pedido[1])
total = lanche * qtd

print(f'Total: R$ {total:.2f}')
