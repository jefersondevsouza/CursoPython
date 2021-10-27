sexo = str(input('Por favor, digite seu sexo [M/F]: ')).upper()
while sexo not in ['F', 'M']:
    sexo = str(input('Dados inválidos. Por favor, digite seu sexo [M/F]: ')).upper()
print('Sexo {} registrado.'.format(sexo))
print('FIM')
