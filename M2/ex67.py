count = 0
total = 0
while True:
    n = int(input('informe um número para tabuada [-1 para parar] : '))
    if(n < 0):
        break
    for c in range(0, 11):
        print('{} x {} = {}'.format(n, c, c*n))
print('FIM')

