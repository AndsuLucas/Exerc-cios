# ler n elementos e armazenar em uma lista
# armazenar em outras duas listas distintas: os números par e ímpar
import time
lista = []
par = []
impar = []

while True:
    lista.append(int(input('insira um número:')))

    while True:
        funcao = str(input('quer continuar? [s/n]:'))

        if funcao == "n" or funcao == "s":
            break

    if funcao == "n":

        break

for v in (lista):
    time.sleep(1)
    print('''Analisando .........''')
    if v % 2 == 0:

        par.append(v)
    else:

        impar.append(v)

print(f'lista criada {lista}')
print(f'números pares:{par}')
print(f'numeros impares:{impar}')

