#leia nome e peso = lista
# quantas pessoas cadastradas
#pessoas mais pesadas
#pessoas mais leves
aux = []
cadastro = []
maispesados = float
funcao = str()
nomepesado = []
nomeleve = list()
maisleve = float
while True:

    aux.append(input('Insira o nome:'))
    aux.append(int(input('Insira o peso:')))
    cadastro.append(aux[:])
    aux.clear()
    while True:
        funcao = input('quer continuar,sim ou não ? [s/n]')
        if funcao =="s" or funcao == "n":
            break

    if funcao == "n":
        break

for pessoa in cadastro:
    aux.append(pessoa[1])



maispesados = (max(aux))

maisleve = (min(aux))

for pessoa in cadastro:
    if maispesados == pessoa[1]:
        nomepesado.append(pessoa[0])
    if maisleve == pessoa[1]:
        nomeleve.append(pessoa[0])

print("=-"*30)

print(f'Quantidade de pessoas cadastradas: {len(cadastro)}')
print(f'O(s) mais leves são: {nomeleve}')
print(f'O(s) mais pesados são:{nomepesado}')













