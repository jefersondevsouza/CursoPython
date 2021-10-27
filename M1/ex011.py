largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = largura * altura
tinta = area / 2
print('Considerando a largura da parede com {} metros e a altura com {} metros:\nTemos uma area de {} m2 e serão necessario {} litros de tinta para pintá=la'.format(largura, altura, area, tinta))
