prim = float(input('Digite a primeira nota: '))
seg = float(input('Digite a segunda nota: '))
media = (prim + seg) / 2
print('Tirando {:.1f} e {:.1f}, a media do aluno é {:.1f}'.format(prim, seg, media))
if media >= 7:
    print('Aluno APROVADO!')
elif media > 5 and media < 7:
    print('Aluno esta de RECUPERAÇÃO')
else:
    print('Aluno esta reprovado')
