import math
notasDisponiveis = [50, 20, 10, 1]
print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)
valor = int(input('Digite o valor que deseja sacar: R$'))
for c in range(0, 4):
    if valor > 0:
        nota = notasDisponiveis[c]
        notas = math.trunc(valor / nota)
        valor = valor - (notas * nota)
        if notas > 0:
            print('Total de {} cédulas de R${}'.format(notas, nota))
print('=' * 30)
print('Volte sempre ao BANCO CEV. Tenha um bom dia!')
