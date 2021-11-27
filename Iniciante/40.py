class Aluno:
    def __init__(self, n1, n2, n3, n4, exame=0):
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4
        self.media = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1) / 2 + 3 + 4 + 1
        self.exame = exame

    def exibe_media(self):
        return self.media

    def media_final(self):
        return self.media + self.exame
    
entrada1 = input().split()
entrada2 = float(input())

# a1 = Aluno()

'''
def media(valores) -> float:
    soma = [0, 0]
    for i in valores.values():
        soma[0] += i[0] * i[1]
        soma[1] += i[1]
    media = soma[0] / soma[1]
    return media 

entrada = input().split()
notas = {
    'n1' : (float(entrada[0]), 2),
    'n2' : (float(entrada[1]), 3),
    'n3' : (float(entrada[2]), 4),
    'n4' : (float(entrada[3]), 1),
}
m = media(notas)
print(f'Media: {m:.1f}')
if (len(entrada) > 4) and (7 > m):
    print('Aluno em exame.')
    nova_media = m + int(entrada[4])
    if nova_media > 7:
        print('Aluno aprovado')
    else:
        print('Aluno reprovado')
    print(f'Media final: {nova_media:.1f}')
elif m > 7:
    print('Aluno aprovado')
else:
    print('Aluno reprovado')
'''