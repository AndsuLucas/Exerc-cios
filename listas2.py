#listas dentro das listas hahahahahah!
galera = []
dado = []

for c in range(0, 3):
    dado.append(input('insira o nome'))
    dado.append(int(input('insira a idade')))
    galera.append(dado[:])
    dado.clear()

print(galera)

for p in galera:

    if p[1] > 18:
        print("oi")