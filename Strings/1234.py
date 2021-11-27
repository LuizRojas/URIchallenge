def string_dancante(string) -> str:
    string = string.lower()
    contador = 0
    caracteres = []
    for i in string:
        if i == ' ':
            caracteres.append(i)
            continue
        else:
            if (contador % 2 == 0):
                caracteres.append(i.upper())
            elif (contador % 2 != 0):
                caracteres.append(i.lower())
        contador += 1
    nova_string = ''.join(caracteres)
    return nova_string


while True:
    entrada = str(input())
    if entrada in 'Zz':
        print(entrada.upper())
        break
    nova_entrada = string_dancante(entrada)
    print(nova_entrada)

# segundo o URI, o programa está apresentando saídas erradas :(
