num = int(input('Digite um número inteiro: '))
count = 0
ehPrimo = 'SIM'
for c in range(1, num + 1):
    if(num % c == 0):
        count += 1
        print('\033[33m', end='')
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='' )
print('\n\033[m', end='')
if count != 2:
    ehPrimo = 'NÃO'
print('O número {} {} é primo'.format(num, ehPrimo))

