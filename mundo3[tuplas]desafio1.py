# desafio 1 0 a 20
tupla = ('zero', 'um', 'dois', 'três', 'quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','desesseis','dezessete','dezoito','dezenove','vinte')



while True:
    numero = int(input('insira um número entre 0 e 20:'))
    if numero>=0 and numero <=20:
        break

print(f'número por extenso = {tupla[numero]}')