count = 0
total = 0
while True:
    n = int(input('informe um número [999 para parar] : '))
    if(n == 999):
        break
    count += 1
    total += n
print('Você digitou {} números e o somatório deles é {}.'.format(count, total))
print('FIM')

