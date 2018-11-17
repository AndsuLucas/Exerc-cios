# nome
# media
# sitação

dc = dict()

dc['nome']  = str(input('insira o nome do aluno:'))
dc['media'] = float(input('insira a média do aluno:'))


if dc['media'] >= 7:
    dc['situação'] = 'aprovado'
else:
    dc['situação'] = 'reprovado'

for en,v in dc.items():
    print(f'{en} : {v}')

