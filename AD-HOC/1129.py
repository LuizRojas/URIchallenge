def verifica_questao(alternativas):
    alternativa = '*'  # alternativa que sera retornada
    alt_marcadas = []
    
    for letra, i in enumerate(alternativas):
        if alternativa == '*' and (i <= 127):
            alternativa = chr(65 + letra)
            alt_marcadas.append(alternativa)
        
        elif alternativa != '*':
            alternativa = '*' # caso haja mais de uma escolha em uma questao, será considerada como rasurada ou "*"

    if len(alt_marcadas) > 1:
        return '*'
    else:
        return alternativa, alt_marcadas

rodando = True
while rodando:
    iteracoes = int(input())
    if iteracoes == 0:
        rodando = False
    
    for i in range(iteracoes):
        questao = str(input()).split()
        questao = [int(x) for x in questao]  # convertendo para numeros inteiros
        
        escolha = verifica_questao(questao)
        print(escolha)
