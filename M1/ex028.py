from random import randint
from time import sleep
nAle = int(randint(0, 5))
nUsua = int(input('O programa escolheu um número entre 0 e 5. Tente adivinhar qual foi: '))
print('PROCESSANDO!')
sleep(3)
if nUsua < 0 or nUsua > 5:
    print('Não avacalha e informe um número válido!')
elif nUsua == nAle:
    print('Muito bem, esse foi o número escolhido. PARABÉNS!!')
else:
    print('Infelizmente você errou, o número escolhido foi {}. Tente novamente.'.format(nAle))
print('Fim programa')
