print('Vamos criar agora uma progressão aritmetica :)')
primTerm = int(input('Digite o primeiro termo: '))
razao = int(input('Digite agora a razão: '))
decimoTermo = (10 * razao) + primTerm
for c in range(primTerm, decimoTermo, razao):
    print(c, end=' -> ')
print('FIM')


