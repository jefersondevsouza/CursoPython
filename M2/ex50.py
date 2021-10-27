soma = 0
valor = 0
for c in range(0, 6):
    valor = int(input('Digite o valor {}: '.format(c + 1)))
    if(valor % 2 == 0):
        soma += valor
print('A soma dos valores pares digitados é: {}'.format(soma))