import time

numero = int(input('insira o número :'))

razao = int(input('insira a razão da p.a:'))

termo = int(input('até qual termo deseja ir ?:'))

resultado = 0

for contador in range(0, termo):
    time.sleep(0.5)
    print(numero)
    numero = numero + razao



