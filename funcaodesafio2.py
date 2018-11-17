# funcao chamada "escreva"
# escreva recebe a mensagem que quer escrever
# linhas adaptaveis conforme o tamanho da string

def escreva(msg):

    print('-'*len(msg))
    print(msg)
    print('-'*len(msg))

for c in range(0,3):
    escreva(input('insira sua mensagem:'))



