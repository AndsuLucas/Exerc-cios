#funcao contador que recebe tres parâmtros : inicio, fim e passo.
#o programa deve realizar as contagens através das funções
# contando de 0 até 10 de 1 em 1
#  contando  de 10 ate 1 de 2 em 2
# personalizado
from time import sleep
def contador(i, f, p):
    print('\n')
    print(f'Contagem de {i} ate {f} de {p} em {p}:')

    if p < 0 :
        p*= -1

    if i > f:
        for c in range(i,f-1,-p):

            print(c,end=" ", flush=True)
            sleep(0.5)
    else:
        for c in range(i,f+1,p):

            print(c, end=" ", flush=True)
            sleep(0.5)







contador(1,10,1)
contador(10,0,2)
print('\n')
print('\nAgora cria sua contagem!')

contador((int(input('inicio:'))),(int(input('fim:'))),(int(input('passo:'))))

