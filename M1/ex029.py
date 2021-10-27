vel = int(input('Informe a velocidade do carro: '))
if(vel <= 80):
    print('Okay, tudo normal.')
else:
    print('Você esta acima do limite de velocidae e foi multado.')
    valorMulta = (vel - 80) * 7
    print('O valor da multa é de R${:.2f}'.format(valorMulta))
print('FIM PROGRAMA')

