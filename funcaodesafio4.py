#funcao maior: recebe vários parâmetros
#dizer qual o maior passado
from time import sleep as s

def maior(*lst):

    max1 = 0

    print(f'Os números informados foram:{lst}')

    print('Analisando...')

    s(5)
    for n,c in enumerate(lst):

        if n == 0:

            max1 = c

        else:

            if c > max1:

                max1 = c

    print(f'O maior número é {max1}')







