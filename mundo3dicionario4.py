from time import sleep
#quantas pessoas foram cadasradas,média de idade, quntas mulheres,pessoas acima da media
f = 0
funcao = str
contador = 0
cadastrototal = []
dc = dict()
soma = 0
am = 0
while True:
    contador+=1
    dc['nome'] = str(input('nome:'))

    while True:
        dc['sexo'] = str(input('sexo: [M/F]')).upper()[0]
        if dc['sexo'] == "M" or dc['sexo'] == "F":
            break

    dc['idade'] = int(input('idade:'))

    cadastrototal.append(dc.copy())

    funcao = str(input('deseja continuar? [s/n]'))

    if funcao == "n":
        break

for c in (cadastrototal):
    soma+= c['idade']
    if c['sexo'] == "F":
        f+=1


media =float( soma/contador)




sleep(1)
print(f'Foram cadastradas {contador} pessoas.')
sleep(1)
print(f'Média de idade: {media}.')
sleep(1)
print(f'Foram cadastradas {f} mulheres.')
sleep(1)
print('Pessoas acima da média>')
for c in (cadastrototal):
    if c['idade']>media:
        sleep(1)
        print(f'{c["nome"]} com {c["idade"]} anos')
        am+=1
print(f'Ao todo {am} pessoas acima da média.')