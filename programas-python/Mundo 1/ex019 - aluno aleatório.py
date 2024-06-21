import random
alu1 = str(input('1º Aluno: '))
alu2 = str(input('2º Aluno: '))
alu3 = str(input('3º Aluno: '))
alu4 = str(input('4º Aluno: '))
lista = [alu1, alu2, alu3, alu4]
escolhido = random.choice(lista)
print('O nome escolhido foi {}'.format(escolhido))
