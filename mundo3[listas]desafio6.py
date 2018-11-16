#equação certa ou errada.

equacao = input('insira a equação:')



lista = []

for c in range(0,len(equacao)):
    lista.append(equacao[c])

contador1 = lista.count("(")
contador2 = lista.count(")")

if (contador1+contador2)%2 == 0:
    print('equação correta!')
else:
    print('equação errada!')
