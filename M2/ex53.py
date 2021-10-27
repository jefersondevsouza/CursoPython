frase = str(input('Digite uma frase qualquer: '))
frase = frase.lower().replace(" ", "")
inverso = frase[::-1]
print('O inverso da frase {} é {}'.format(frase, inverso))
if(inverso == frase):
    print('Temos um palíndromo')
else:
    print('A frase digitada Não é um palindromo')
