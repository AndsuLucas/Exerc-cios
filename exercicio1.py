# crime

suspeito = []

while True:
    print('Por favor, responda apenas: (sim) ou (não) para as perguntas.')
    print("-"*30)



    suspeito.append(input('já telefonou para a vitima?:'))

    suspeito.append(input('já esteve no local do crime?:'))

    suspeito.append(input('já morou perto da vítima?:'))

    suspeito.append(input('já deveu algo para a vítima?:'))

    suspeito.append(input('já trabalhou com a vítima?:'))


    print(suspeito)
    print(suspeito.count('sim')+suspeito.count('não'))
    if suspeito.count('sim')+suspeito.count('não') ==5:
        break

    else:
        print('Por favor, apenas responda (sim) ou (não) para as perguntas.')

    print("-"*30)

if suspeito.count("sim")==2:
    print("Você é suspeito.")
elif suspeito.count("sim")>=3 and suspeito.count("sim")<=4:
    print("Você é cumplice.")
elif suspeito.count("sim")==5:
    print("Você é o assasino!")
else:
    print("Você é inocente.")