print('Diginte somente números inteiros')
prim = int(input('Primeiro numero: '))
seg = int(input('Segundo numero: '))
if(prim > seg):
    print('Primeiro número é maior que o segundo')
elif seg > prim :
    print('Segundo número é maior que o primeiro')
else:
    print('Ambos os números são iguais')
