ret1 = float(input('Digite o comprimento da primeiro reta: '))
ret2 = float(input('Digite o comprimento da segundo reta: '))
ret3 = float(input('Digite o comprimento da terceiro reta: '))
prov = ret2 + ret3
lado1Ok = (ret1 < prov) & (ret1 > float(prov - ret1))
prov = ret1 + ret3
lado2Ok = (ret2 < prov) & (ret2 > float(prov - ret2))
prov = ret1 + ret2
lado3Ok = (ret3 < prov) & (ret3 > float(prov - ret3))
if lado1Ok | lado2Ok | lado3Ok:
    print('É um triângulo sim.')
else:
    print('Não é um triângulo.')
print('FIM PROGRAMA')
