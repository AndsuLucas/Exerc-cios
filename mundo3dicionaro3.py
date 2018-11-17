import time


#mostrar com quantos anos a pessoa vai se aposentar.

anoatual = int(2018)
dc = dict()
ap = int(35)
dc['nome'] = str(input('nome:'))
dc['ano de nascimento'] = int(input('ano de nascimento:'))

dc['idade'] = anoatual - dc['ano de nascimento']

dc['CTPS'] = int(input('Carteira de trabalho:'))

if dc['CTPS'] > 0 :
    dc['ano de contratação'] = int(input('insira o ano da sua contratação:'))
    aux = (anoatual - dc['ano de contratação'])
    dc['idade ao aposentar'] = int(dc['idade']+(ap-aux))
else:
    del dc['CTPS']
print('-='*30)

for k,v in dc.items():

    time.sleep(1)
    print(f'{k} : {v}')



