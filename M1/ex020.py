from random import choice, shuffle
aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')
listaAlunos = [aluno1, aluno2, aluno3, aluno4]
shuffle(listaAlunos)
print('A ordem de apresentação será')
print(listaAlunos)