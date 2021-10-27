num = 0
count = 0
total = 0
while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    if num != 999:
        total += num
        count += 1
print('Você digitou {} numeros, e o total foi {}'.format(count, total))

