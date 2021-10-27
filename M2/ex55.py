maior = 0
menor = 0
for c in range(0, 5):
    peso = float(input('Informe o peso {}: '.format(c + 1)))
    if(maior == 0 or peso > maior):
        maior = peso
    if(menor == 0 or peso < menor):
        menor = peso
print('O maior peso é {} e o menor peso é {}'.format(maior, menor))