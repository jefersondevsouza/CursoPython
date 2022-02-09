tuplaBasileiro = (
'Atletico Mineiro', 'Palmeiras', 'Bragantino', 'Fortaleza', 'Flamengo', 'Internacional', 'Corintians', 'Fluminense',
'Atletico Goianiense', 'America Mineiro', 'Cuiaba', 'Athletico-PR', 'Sao Paulo', 'Ceara', 'Bahia', 'Santos',
'Juventude', 'Sport Recife', 'Gremio', 'Chapecoense')
print('Esses são os times do Brasileirão {}'.format(tuplaBasileiro))
print('Os primeiro 5 colocados são {}'.format(tuplaBasileiro[:5]))
print('Os últimos 4 colocados são {}'.format(tuplaBasileiro[16:]))
print('Lista dos times em ordem alfabética {}'.format(sorted(tuplaBasileiro)))
print('O time da Chapecoense está {}ª posição da tabela.'.format(tuplaBasileiro.index('Chapecoense') + 1))
