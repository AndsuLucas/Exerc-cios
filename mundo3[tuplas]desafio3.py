def funcao():

    return int(input('insira um número:'))
tupla = (funcao(), funcao(), funcao(), funcao())

print(tupla.count(9))

print(tupla)

print(f'{tupla:.<30}')