valorCompra = float(input('Valor das compras: R$'))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/ cheque')
print('[ 2 ] à vista no cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
opcao = int(input('Qual é a opção: '))
if(opcao == 1):
    desconto = 10
    valorFinal = valorCompra - (valorCompra / 100 * desconto)
    print('Sua compra de {:.2f} vai sair a {:.2f} com {}% de desconto.'.format(valorCompra, valorFinal, desconto))
elif(opcao == 2):
    desconto = 5
    valorFinal = valorCompra - (valorCompra / 100 * desconto)
    print('Sua compra de {:.2f} vai sair a {:.2f} com {}% de desconto.'.format(valorCompra, valorFinal, desconto))
elif(opcao == 3):
    print('Sua compra de {:.2f} vai sair a {:.2f} em 2x de {:.2f}.'.format(valorCompra, valorCompra, valorCompra / 2))
elif(opcao == 4):
    parcelas = int(input('Quantas parcelas: '))
    acrescimo = 20
    valorFinal = valorCompra + (valorCompra / 100 * acrescimo)
    print('Sua compra de {:.2f} vai sair a {:.2f} em {}x de {:.2f} com {}% de acréscimo.'.format(valorCompra, valorFinal, parcelas, (valorFinal / parcelas), acrescimo))
else:
    print('Opção inválida')

