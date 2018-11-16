cintquenta =int(0)
vinte =int (0)
dez =int (0)
um = int(0)

resto = int(0)

saque = int(input('insira o valor do saque:'))

while True:
    cinquenta = int(saque/50)
    if saque%50 !=0:
        resto = saque%50
    else:
        break
    vinte = int(resto/20)
    if saque%20 !=0:
        resto = saque%20
    else:
        break

    dez = int(resto/10)

    if saque%10 != 0:
        resto = saque%10
    else:
        break

    um = int(resto/1)
    if resto%1 ==0:
        break
print('-----------------------------------')

print(f'notas de 50: {cinquenta}')
print(f'notas de 20: {vinte}')
print(f'notas de 10: {dez}')
print(f'notas de 1: {um}')
