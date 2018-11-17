# lista = números
# 2 funcoes: sorteio e par
# funcao sorteio: sorteia 5 numeros
# funcao par: soma os números ímpares.
from random import randint as rd

def sorteio(lst=list):

    for c in range(0,5):
        lst.append(rd(1,100))


    print(f'Os números sorteados foram {lst}')

def par (lst=list):
    soma = 0


    for e in (lst):
        if e % 2 == 0:
            soma+= e

    print(f'A soma dos elementos pares presentes na {lst} é = {soma} ')





lista = []

sorteio(lista)
par(lista)



