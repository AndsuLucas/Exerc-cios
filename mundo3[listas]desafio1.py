# 5 valores e botar em uma lista
# mostrar o maior valor e menor valor  e suas posições.
# aqui estou utiliizando meu algoritmoo para testes

from testex import teste

lista = list()


for c,v in enumerate(range(0,30)):
    #lista.append(int(input(f'insira um número na posição {c+1}:')))
    lista.append(teste())



print(lista)

print("=-"*20)
print(f'o maior valor é: {max(lista)}, sua posição é a {lista.index(max(lista))+1}ª')
print(f'o menor valor é: {min(lista)}, sua posição é a {lista.index(min(lista))+1}ª')
print("=-"*20)
