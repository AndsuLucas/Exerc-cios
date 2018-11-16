#matriz 3x3 > preencher com os números lidos

matriz = [[], [], []]

for c,elemento in enumerate(matriz):

    for contador in range(0,3):
        matriz[c].append(int(input(f'insira o número na posição {c},{contador}')))


print("=-"*30)

print(matriz[0])
print(matriz[1])
print(matriz[2])

print("=-"*30)