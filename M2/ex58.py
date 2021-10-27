from random import randint
print('Olá')
print('Sou o seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
computador = randint(0, 10)
print('Será que você consegue adivinhar qual foi?')
usuario = int(input('Qual o seu palpite? '))
tentativas = 1
while(computador != usuario):
    tentativas += 1
    if(computador > usuario):
        print('Mais... ', end='')
    else:
        print('Menos... ', end='')
    print('Tente mais uma vez.')
    num = int(input('Qual o seu palpite? '))
print('Show de bola, você descobriu o número {}, que escolhi em {} tentativas.'.format(computador, tentativas))



