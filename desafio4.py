
ano_nascimento = int(input('insira o ano do seu nascimento:'))
ano_atual= (2018)

idade = ano_atual - ano_nascimento


if(idade<=9):
    print('nadador mirim')

elif(idade<=14):
    print('nadador infantil')

elif(idade<=19):
    print('nadador junior')

elif(idade==20):
    print('nadador senior')

else:
    print('nadador master')