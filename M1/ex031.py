dist = float(input('Digite o valor da distância da viagem em KM: '))
valorPassagem = 0.00
if dist <= 200:
    valorPassagem = (dist * 0.5)
else:
    valorPassagem = (dist * 0.45)
print('O valor de sua passagem é de R${:.2f}'.format(valorPassagem))
print('FIM PROGRAMA')

