preco = float(input('Digite o preço do produto: '))
desconto = 5.0
novopreco = preco - (preco / 100 * desconto)
print('O preco do produto é {}, e aplicando um desconto de {}% temos o novo preco de {}'.format(preco, desconto, novopreco))