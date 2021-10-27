salario = float(input('Digite o valor do salario: '))
aumento = 15.0
novosal = salario + (salario / 100 * aumento)
print('O salário atual é {}, e aplicando um aumento de {}% temos o novo salario de {}'.format(salario, aumento, novosal))
