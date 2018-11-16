# usuario digita 5 numeros  = lista organizados conforme a ordem digitada
# sem usar o sort, ordenar a lista na tela.

lista = []
listafinal =[]

for v in range(0,5):
    lista.append(int(input('insira um número:')))



while True:



    listafinal.append(min(lista))
    lista.remove(min(lista))

    if len(lista)==0:
        break


print(f"sua lista foi ordenada em ordem crescente:{listafinal}")




