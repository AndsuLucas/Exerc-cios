#alistamento

ano_nascimento = int(input('insira sua data de nascimento:'))
ano_atual = (2018)

idade = int(ano_atual - ano_nascimento)

if(idade==18):
    print('é hora de se alistar!')
elif(idade<18):
    troca = (18-idade)
    print('falta(m) {} ano(s) para você se alistar.'.format(troca))
else:
    troca = (idade-18)
    print('você está atrasado em {} ano(s). Precisa se alistar urgentemente!'.format(troca))