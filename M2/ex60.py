numero = int(input('Digite um número para calcular o seu fatorial: '))
valor = 0

if(numero <= 0):
    print('Numero Inválido.')
else:
    valor = 1
    print('Calculando o {}! = '.format(numero), end='')
    while numero > 1:
        print('{} X '.format(numero), end='')
        valor = valor * numero
        numero = numero - 1
    print('1', end='')
    print(" = {}".format(valor))
