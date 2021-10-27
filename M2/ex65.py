num = 0
controle = 's'
count = 0
total = 0
maior = 0
menor = -999999999
while controle == 's':
    num = int(input('Digite um número: '))
    controle = str(input('Quer continuar? [S/N]')).lower().strip()[0]
    count += 1
    total += num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
print('Voce digitou {} números e a média foi {.:2f}'.format(count, total / count))
print('O maior valor foi {} e o menor valor foi {}'.format(maior, menor))
print('FIM')
