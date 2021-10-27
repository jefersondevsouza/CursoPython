num = str(input('Informe um número de 0 a 9999: ')).strip()
numeroForm = ('0000' + num)
numeroForm = numeroForm[len(numeroForm) - 4:]
print('Analisando o número {}'.format(numeroForm))
print('Unidade {}'.format(numeroForm[3]))
print('Dezena {}'.format(numeroForm[2]))
print('Centena {}'.format(numeroForm[1]))
print('Milhar {}'.format(numeroForm[0]))

