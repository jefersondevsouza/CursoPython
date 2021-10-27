print('Gerado de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termpo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
maxCount = 0
proximaIteracao = 10
while proximaIteracao != 0:
    maxCount += proximaIteracao
    while cont <= maxCount:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    proximaIteracao = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(maxCount))
