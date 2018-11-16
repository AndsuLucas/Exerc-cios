import random as rd
import time as tm
#mega sena
lista = []

numero = int(input('quantos jogos você quer que  eu sorteie?:'))

for c in range(0,numero):

    for c2 in range(0,6):

        lista.append(rd.randint(1,100))

    tm.sleep(1)
    print(f'jogo {c+1}:{lista}')

    lista.clear()
