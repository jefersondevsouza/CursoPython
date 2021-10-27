salario = float(input('Digite o valor do salário: R$'))
if salario > 1250:
    print('O salário R${:.2f} passará para {:.2f}, tendo um aumento de 10%'.format(salario, salario * 1.1))
else:
    print('O salário R${:.2f} passará para {:.2f}, tendo um aumento de 15%'.format(salario, salario * 1.15))
print('FIM PROGRAMA')