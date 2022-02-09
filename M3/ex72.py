tuplaNumeros = (
    'Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze',
    'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
print('O programa será interrompido a qualquer momento apertando um caracter inválido')
while (True):
    try:
        numero = int(input('Informe um número de 0 a 20:'))
        if 0 <= numero <= 20:
            print('Você digitou o número ' + tuplaNumeros[numero])
        else:
            print('Número inválido!')
    except:
        print('Caracter não permitido!')
        break
print('Programa finalizado!')
