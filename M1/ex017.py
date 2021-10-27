cateOp = float(input('Informe o valor do cateto oposto: '))
cateAd = float(input('Informe o valor do cateto adjacente: '))
hip = ((cateOp**2) + (cateAd**2)) ** (0.5)
print('O comprimento da hipotenusa = {:.2f}'.format(hip))
