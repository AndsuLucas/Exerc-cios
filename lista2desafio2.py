# sete valores numéricos =  entrada
# em uma única lista separar os pares dos ímpares
# mostrar os valoresem ordem crescente no final

lista = []
aux1 = []
aux2 = []
for contador in range (0,7):
    lista.append(int(input('Insira um número inteiro:')))

for c,imp in enumerate(lista):
    if imp % 2 != 0 :
        aux1.append(lista[c])

for c2,par in enumerate(lista):

    if par %2 == 0:
        aux2.append(lista[c2])

lista.clear()
lista.append(aux1[:])
lista.append(aux2[:])
print(lista)

