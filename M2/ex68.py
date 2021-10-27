from random import randint
print('=-' * 30)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-' * 30)
count = 0
total = 0
perdi = False
while not perdi:
    escolha = str(input('Par ou impar? [P/I]')).upper()[0]
    if escolha in ['P', 'I']:
        numero = int(input('Digite um número inteiro: '))
        print('--' * 30)
        computador = randint(0, 5)
        print('Voce jogou {} e o computador jogou {}'.format(numero, computador))
        print('Total de {}'.format(numero + computador))
        resultado = ((numero + computador) % 2) == 0
        if resultado:
            print('DEU PAR')
        else:
            print('DEU IMPAR')
        print('--' * 30)

        if (escolha == 'P') & (resultado) | (escolha == 'I') & (not resultado):
            print('VOCE VENCEU')
            count += 1
        else:
            print('VOCE PERDEU')
            perdi = True
        print('=-' * 30)
    else:
        print('Opção inválida, tente novamente.')
print('GAME OVER! Você venceu {} vezes.'.format(count))
