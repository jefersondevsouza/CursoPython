produtoMaisBarato = ' '
valorProdutoMaisBarato = 0
produtosMaisDe1000 = 0
totalCompra = 0
print('=~' * 30)
print('LOJA DO SUPER BARATÃO')
print('=~' * 30)
while True:
    print('--' * 30)
    print('Informe o produto')
    print('--' * 30)
    produto = str(input('Produto: '))
    preco = float(input('Valor: R$'))
    totalCompra += preco
    if preco >= 1000:
        produtosMaisDe1000 += 1
    if (valorProdutoMaisBarato == 0) or (preco < valorProdutoMaisBarato):
        valorProdutoMaisBarato = preco
        produtoMaisBarato = produto
    continua = ''
    while continua not in ['S', 'N']:
        continua = str(input('Deseja continuar: [S/N] ')).upper()[0]
        if continua not in ['S', 'N']:
            print('Opção inválida. Tente novamente.')
    if continua == 'N':
        break
print('--' * 30)
print('FECHANDO A CONTA')
print('--' * 30)
print('O total gasto na compra foi de {}'.format(totalCompra))
print('Você comprou {} produto com valor superior a R$1000,00. '.format(produtosMaisDe1000))
print('O produto mais barato foi o {} e custou R${}.'.format(produtoMaisBarato, valorProdutoMaisBarato))


