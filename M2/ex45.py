from random import randint
from time import sleep
opcoes = ['Pedra', 'Papel', 'Tesoura']
print('{:=^40}'.format('Jokenpo'))
print('[ 0 ] Pedra')
print('[ 1 ] Papel')
print('[ 2 ] Tesoura')
jogador = int(input('Qual é a opção: '))
if(jogador == 0 or jogador == 1 or jogador == 2):
    sistema = randint(0, 2)
    sleep(.5)
    print('JO')
    sleep(.8)
    print('KEN')
    sleep(.8)
    print('PO!!!')
    print('-=' * 11)
    print('Voce escolheu {}'.format(opcoes[jogador]))
    print('O computador escolheu {} '.format(opcoes[sistema]))
    print('-=' * 11)
    if(jogador == 2 and sistema == 1):
        print('Voce venceu!')
    elif(jogador == 1 and sistema == 0):
        print('Voce ganhou!')
    elif(jogador == 0 and sistema == 2):
        print('Voce ganhou!')
    elif(jogador == sistema):
        print('Empate!')
    else:
        print('Você perdeu!')
else:
    print('Opção inválida. Tente novamente')