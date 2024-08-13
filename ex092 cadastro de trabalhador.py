from datetime import datetime
trab = dict()
trab['nome'] = str(input('Nome: '))
trab['nascimento'] = int(input('Ano de Nascimento: '))
trab['idade'] = datetime.now().year - trab['nascimento']
trab['ctps'] = int(input('Carteira de trabalho [0 não tem]: '))
if trab['ctps'] != 0:
    trab['contratação'] = int(input('Ano de contratação: '))
    trab['salário'] = float(input('Salário: R$'))
    trab['aposentadoria'] = 35 + trab['contratação'] - trab['nascimento']
for k, v in trab.items():
    print(f' - {k} tem o valor {v}')

