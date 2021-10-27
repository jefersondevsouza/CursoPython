from datetime import date
anoAtual = date.today().year
maior = 0
menor = 0
for c in range(0, 7):
     ano = int(input('Digite o ano de nascimento {}: '.format(c + 1)))
     if(anoAtual - ano >= 21):
        maior+=1
     else:
         menor+=1
print('{} pessoas são maior de idade e {} pessoas são menor de idade'.format(maior, menor))