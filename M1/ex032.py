from datetime import date
ano = int(input('Digite um ano qualquer para saber se é bissexto. Informe 0 para o ano atual: '))
if(ano == 0):
    ano = date.today().year
if (ano % 4 == 0):
    if(ano % 100 > 0):
        print('Ano {} foi bissexto.'.format(ano))
    elif(ano % 400 == 0):
        print('Ano {} foi bissexto.'.format(ano))
    else:
        print('Ano {} não foi bissexto.'.format(ano))
else:
    print('Ano {} não foi bissexto.'.format(ano))
print('FIM PROGRAMA')

