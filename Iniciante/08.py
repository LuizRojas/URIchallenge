funcionario = dict()

funcionario['numero'] = int(input())
funcionario['horas'] = int(input())
funcionario['valor hora'] = float(input())

salario = funcionario['valor hora'] * funcionario['horas']

print(f'NUMBER = {funcionario["numero"]}\nSALARY = U$ {salario:.2f}')
