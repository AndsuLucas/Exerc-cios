numero = int(input('insira um número inteiro:'))

auxiliar = numero

for c in range(auxiliar, 1, -1):

    auxiliar = auxiliar - 1
    numero = numero * auxiliar
    print(numero)

if numero == 0:
    print("1")







