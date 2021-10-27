frase = str(input('Escreva uma frase: ')).strip().lower()
numA = frase.count('a')
pos1A = frase.find('a') + 1
posFA = frase.rfind('a') + 1
print('A frase digitada possui {} letras A.'.format(numA))
print('A primeira ocorrência da letra A esta na posição {}'.format(pos1A))
print('A última ocorrência da letra A esta na posição {}'.format(posFA))