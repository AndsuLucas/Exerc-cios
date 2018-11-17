#gerenciar aproveitamento jogador
#ler: nome, aproveitamento do jogador gols por partida
# guardar em biblioteca ; os gold são listas
from time import sleep
gols = []
dc = dict()
soma = 0

dc['Nome'] = str(input('nome do jogador:'))

partidas = int(input('partidas jogada:'))

for c in range(0,partidas):

    gols.append(int(input(f'insira quantos gols o jogador fez na partida {c+1}')))
    soma = (gols[c] + soma)

dc['Gols'] = gols [:]

dc['Total'] = soma

print('-='*30)
print(dc)
print('-='*30)

for c,e in dc.items():
    sleep(1)
    print(f'{c}:  {e}')

print('=-'*30)
sleep(1)
print(f'O jogador {dc["Nome"]} jogou {partidas} partidas.')

for c in range (0,partidas):
    sleep(1)
    print(f'   Na partida {c+1} o jogador marcou {dc["Gols"][c]} gols.' )


print(f'Total de gols marcados: {soma}')