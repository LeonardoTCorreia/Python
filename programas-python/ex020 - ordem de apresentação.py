from random import shuffle
alu1 = str(input('1º Aluno: '))
alu2 = str(input('2º Aluno: '))
alu3 = str(input('3º Aluno: '))
alu4 = str(input('4º Aluno: '))
alunos = [alu1, alu2, alu3, alu4]
shuffle(alunos)
print('A ordem de apresentação dos trabalhos é: \n')
print(alunos)

