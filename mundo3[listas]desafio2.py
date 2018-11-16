#lista= digite vários valores númericos conforme a sua vontade
# se o número existir, o valor não ser adicionado
contador = 0
lista = []
funcao = str
while True:

    x = (int(input("insira um número:")))

    if x in lista :
        print('número repitido...')


    else:
        lista.append(x)
        print('número adicionado...')

    funcao = str(input('deseja continuar, sim ou não [s/n]?:'))

    if funcao == "n":
        break

print(f'números válidos adicionados{sorted(lista)}')