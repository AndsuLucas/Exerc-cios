# ordenar uma quantidade x de números em uma lista de forma decrescente, mostrar quantas vezes o número 5 foi digitado
# mostrar tamanho da lista.
lista = []

while True:
    lista.append(int(input('insira um número:')))

    while True:
        funcao = str(input('quer continuar colocando números na lista? [s/n]:'))

        if funcao=="s" or funcao == "n":
            break


    if funcao == "n":
        break


lista.sort(reverse=True)

print(f'lista ordenada de forma decrescente: {lista}')
print(f'foram digitados {len(lista)} números')
print(f'o valor 5 foi digitado {lista.count(5)}x.')