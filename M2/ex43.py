peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é o sua altura? (m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {}'.format(imc))
if imc < 18.5:
    print('IMC abaixo de 18,5: abaixo do peso.')
elif imc < 25:
    print('PARABENS, voce esta na faixa de peso NORMAL')
elif imc < 30:
    print('IMC acima de 25: Sobrepeso.')
elif imc < 40:
    print('IMC acima de 30: Obesidade.')
else:
    print('IMC acima de 40: Obesidade Mórbida.')
