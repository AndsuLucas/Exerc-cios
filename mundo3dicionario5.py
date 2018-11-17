#partidas gols e jogadores.
#mais de um jogador
from time import sleep
gols = []
lista = []
dc = dict()
partidas = 0
tt = int()

while True:

    dc['nome'] = str(input('nome:'))

    partidas = int(input('quantas partidas ele jogou?'))

    for c in range(0,partidas):

        gols.append(int(input(f'Quantos gols na partida {c+1}')))

        tt+= gols[c]

    dc['gols']= gols[:]

    gols.clear()

    dc['total'] = tt

    lista.append(dc.copy())

    funcao = str(input('deseja continuar? [S/N]')).upper()[0]

    if funcao in "N":
        break
print('=-'*30)
print('Cod Nome          Gols     total')
for n,e in enumerate(lista):
    sleep(1)

    print(f'{n:>2}  {e["nome"]}    {e["gols"]}       {e["total"]}')
#fica pra proxima.