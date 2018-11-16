#//desafio 1
#//empréstimo

    #//dados de entrada
casa = float(input('insira o valor da casa que deseja comprar:'))
sal = float(input('insira seu salário:'))
per = float(input('insira o tempo que deseja quitar seu empréstimo. [EM ANOS]:'))

#//processamento
    #//valor mensal a ser pago
vm = (casa/(12*per))
    #//30% do salário
teste = (sal*(30/100))

#//teste condicional
    #//tedste de aprovação do empréstim
if(vm>teste):
        #//VM excede TESTE
    print('Empréstimo negado. Pois o valor mensal:{:.2f} excede 30% do seu salário:{:.2f}'.format(vm,teste))
else:
        #//VM não excede TESTE
    print('Empréstimo aprovado.')


