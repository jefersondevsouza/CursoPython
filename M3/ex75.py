
tuplaValores = (int(input('Digite o 1ª valor: ')), int(input('Digite o 2ª valor: ')),
                int(input('Digite o 3ª valor: ')), int(input('Digite o 4ª valor: ')))
print('Você digitou os seguintes números {}'.format(tuplaValores))
print('O número 9 foi informado {} vezes'.format(tuplaValores.count(9)))
if 3 in tuplaValores:
    index3 = tuplaValores.index(3)
    print('O número 3 apareceu a primeira vez na posição {}'.format(index3 + 1))
else:
    print('O número 3 não foi digitado nenhuma vez')
contaPar = 0
for num in tuplaValores:
    if(num % 2 == 0):
        contaPar += 1
print('Foram digitados {} números pares.'.format(contaPar))
print('Fim programa')
