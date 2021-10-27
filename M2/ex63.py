print('-' * 30)
print('Sequência de Finonacci')
print('-' * 30)
n = int(input('Quantos termos você quer mostrar: '))
count = 2
nFibo1 = 0
nFibo2 = 1
print('~'*30)
print('{} -> {} -> '.format(nFibo1, nFibo2), end='')
while count < n:
    print('{} -> '.format(nFibo1 + nFibo2), end='')
    fibo = nFibo1 + nFibo2
    nFibo1 = nFibo2
    nFibo2 = fibo
    count += 1
print('FIM')
print('~'*30)
