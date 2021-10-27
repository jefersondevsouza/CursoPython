from datetime import date
print('Escolha seu genero:')
print('[ 1 ] Masculino')
print('[ 2 ] Feminino')
genero = int(input('Escolha o genero: '))
if(genero == 1 ):
    anoNascimento = int(input('Ano de nascimento: '))
    anoAtual = date.today().year
    idade = anoAtual - anoNascimento
    print('Quem nasceu em {} tem {} em {}'.format(anoNascimento, idade, anoAtual))
    if(idade == 18):
        print('Voce deve se alistar IMEDIATAMENTE')
    elif idade < 18:
        anosfalta = 18 - idade
        print('Ainda faltam {} anos pra voce se alistar. Voce devera se alistar em {}'.format(anosfalta, anoAtual + anosfalta))
    else:
        anosPassou = idade - 18
        print('Ja se passaram {} anos do seu alistamento. Vode devia ter se alistado em {}'.format(anosPassou, anoAtual - anosPassou))
elif genero == 2:
    print('Mulheres não precisam se alistar')
else:
    print('Opção inválida')
