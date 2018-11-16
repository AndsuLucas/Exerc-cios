#tabuada

import time

numero = int(input('insira o número para saber sua tabuada:'))

for aux in range(0,11):
    time.sleep(1)
    print(numero*aux)
