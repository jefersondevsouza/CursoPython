from datetime import date
ano = int(input('Ano de nascimento do atleta: '))
classificacao = ''
anoAtual = date.today().year
idade = anoAtual - ano
print('O atleta tem {} anos'.format(idade))
if(idade <= 9):
    classificacao = 'MIRIM'
elif (9 < idade <= 14):
    classificacao = 'INFANTIL'
elif (9 < idade <= 19):
    classificacao = 'JUNIOR'
elif (19 < idade <= 25):
    classificacao = 'SENIOR'
elif (idade > 25):
    classificacao = 'MASTER'
print('Classificação do atleta: {}'.format(classificacao))
