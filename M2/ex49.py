num = int(input('Digite o numero para a tabuada: '))
print('-' * 12)
for c in range(0, 11):
    print('{} * {:2} = {:2}'.format(num, c, (num * c)))
print('-' * 12)
print('FIM')
