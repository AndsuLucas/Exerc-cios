#cada jogador joga um dado = resultados aleatórios
#guardar todos os resultados em um dicionário.
#colocar o dicionário em ordem = vencedor
import time
import random
from operator import itemgetter
rankind = dict()
dc = dict()

dc['jogador1'] = random.randint(1,6)
dc['jogador2'] = random.randint(1,6)
dc['jogador3'] = random.randint(1,6)
dc['jogador4'] = random.randint(1,6)
dc['jogador5'] = random.randint(1,6)

for en,el in dc.items():
    time.sleep(1)
    print(f'{en} : {el}')

rankind = sorted(dc.items(), key=itemgetter(1), reverse=True)

print('-='*30)
for v,c in enumerate(rankind):
    time.sleep(1)
    print(f'{v+1}º lugar -> {c[0]}, número : {c[1]} ')

