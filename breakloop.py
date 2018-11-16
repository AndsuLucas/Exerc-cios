# parar estruturas de repetição infinitas

n = s = 0

while True:
    n = int(input('insira um número:'))

    if n == 10:
        break
    s+= n

print(f'{s}')
