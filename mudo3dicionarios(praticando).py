estado = dict()
brasil = list()

for c in range(0,3):
    estado['uf'] = str(input('insira o estado'))
    estado['sigla'] = str(input('insira a sigla'))
    brasil.append(estado.copy())

for v in brasil:
    for i,j in v.items():
        print(f'{i}:{j}')