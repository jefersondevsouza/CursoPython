nome = str(input('Informe seu nome: ')).strip()
temSilva = nome.upper().find(('SILVA')) >= 0 #pode utilizar o ('SILVA' in nome.upper())
print('Seu nome tem Silva?', temSilva)