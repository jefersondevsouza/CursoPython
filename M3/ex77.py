tupla = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'programador', 'futuro')
for palavra in tupla:
    print(f'A palavra {palavra.upper()} tem as seguintes vogais: ', end='' )
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
    print()
