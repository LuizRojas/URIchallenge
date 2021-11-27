def codifica_string(string: str, valor: int) -> str:
    caracteres = []
    for i in string:
        if (ord(i) + valor) > 90:
            caracter = ord(i) + (-26 + valor)
            caracteres.append(chr(caracter))
        else:
            caracter = ord(i) + valor
            caracteres.append(chr(caracter))
    nova_string = ''.join(caracteres)
    return nova_string


termos = int(input())
for i in range(termos):
    entrada = str(input()).upper()
    salto = int(input())
    print(codifica_string(entrada, salto))
