mediaIdade = 0
nomeHomemMaisVelho = ''
idadeHomemMaisVelho = 0
totalIdades = 0
mulheresMenos20Anos = 0

for c in range(0, 4):
    nome = str(input('Digite o nome da pessoa {}: '.format(c + 1)))
    idade = int(input('Digite a idade da pessoa {}: '.format(c + 1)))
    sexo = str(input('Digite o sexo da pessoa {}: '.format(c + 1)))
    totalIdades += idade
    if(sexo.lower()[0] == 'm'):
        if(idadeHomemMaisVelho == 0 or idade > idadeHomemMaisVelho):
            idadeHomemMaisVelho = idade
            nomeHomemMaisVelho = nome
    elif(sexo.lower()[0] == 'f'):
         if(idade < 20):
             mulheresMenos20Anos +=1
mediaIdade = totalIdades / 4
print('O programa detectou que a média da idade do grupo é {} anos'.format(mediaIdade))
print('O homem mais velho é o {} e possui {} anos'.format(nomeHomemMaisVelho, idadeHomemMaisVelho))
print('No grupo possui {} mulheres com menos de 20 anos'.format(mulheresMenos20Anos))

