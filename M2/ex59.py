
opcao = 4
while opcao != 5:
    if(opcao == 1):
        print('{} + {} = {}'.format(primeiro, segundo, primeiro + segundo))
    elif (opcao == 2):
            print('{} x {} = {}'.format(primeiro, segundo, primeiro * segundo))
    elif (opcao == 3):
            maior = primeiro
            menor = segundo
            if (primeiro == segundo):
                print('Ambos os valores são iguais.')
            else:
                if(segundo > primeiro):
                    maior = segundo
                    menor = primeiro
                print('{} é maior que {}'.format(maior, menor))
    elif(opcao == 4):
        primeiro = float(input('Digite o primeiro valor: '))
        segundo = float(input('Digite o segundo valor: '))
    else:
        print('Opção inválida. Tente novamente.')
    print('[ 1 ] somar')
    print('[ 2 ] multiplicar')
    print('[ 3 ] maior')
    print('[ 4 ] novos números')
    print('[ 5 ] sair do programa')
    opcao = int(input('>>>>>>>>> Qual a sua opção? '))
print('FIM')