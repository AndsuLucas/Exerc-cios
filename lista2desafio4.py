#matriz somando os valores pares.
#soma da terceira coluna
#soma da segunda linha
matriz = [[], [], []]
somapar = int()
somater = int()
linha= ()
for c,elemento in enumerate(matriz):

    for contador in range(0,3):
        matriz[c].append(int(input(f'insira o número na posição {c},{contador}')))

for c,m in enumerate(matriz):
    for a in range(0,3):
        if m[a] % 2 == 0:
            somapar = somapar + m[a]

    somater = somater + m[2]
    linha = sum(matriz[1])



print("=-"*30)

print(matriz[0])
print(matriz[1])
print(matriz[2])

print("=-"*30)

print(somapar)
print(somater)
print(linha)