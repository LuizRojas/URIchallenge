def string_dancante(string) -> str:
    string = string.split()
    nova_string = []
    fatia1, fatia2 = string[0], string[1]
    for primeira, segunda in zip(fatia1, fatia2):
        nova_string.append(primeira)
        nova_string.append(segunda)
    nova_string = ''.join(nova_string)
    return nova_string


entrada = str(input())
print(string_dancante(string=entrada))
