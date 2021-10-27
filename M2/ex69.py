contMais18 = 0
contHomem = 0
contMulher = 0
print('=~' * 30)
print('CADASTRO DE PESSOAS')
print('=~' * 30)
while True:
    print('--' * 30)
    print('Cadastre uma pessoa')
    print('--' * 30)
    sexo = ''
    while sexo not in ['F', 'M']:
        sexo = str(input('Digite o sexo da pessoa: [M/F] ')).upper()[0]
        if sexo not in ['F', 'M']:
            print('Opção inválida. Tente novamente.')
    idade = int(input('Digite a idade da pessoa: '))
    print('--' * 30)
    if sexo == 'M':
        contHomem += 1
    else:
        if idade < 20:
            contMulher += 1
    if(idade >= 18):
        contMais18 += 1
    continua = ''
    while continua not in ['S', 'N']:
        continua = str(input('Deseja continuar: [S/N] ')).upper()[0]
        if continua not in ['S', 'N']:
            print('Opção inválida. Tente novamente.')
    if continua == 'N':
        break
print('Você informou {} pessoas com 18 anos ou mais'.format(contMais18))
print('Você informou {} homens. '.format(contHomem))
print('E você informou {} mulheres com menos de 20 anos'.format(contMulher))


