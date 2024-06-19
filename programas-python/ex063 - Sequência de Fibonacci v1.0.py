print('~'*22)
print('SEQUÊNCIA DE FIBONACCI')
print('~'*22)
termos = int(input('Quantos termos você quer mostrar? '))
p1 = 0
p2 = 1
p3 = 1
contador = 1
print(p1, end=' -> ')
print(p2, end=' -> ')
while contador <= termos - 2:
    p3 = p1 + p2
    print(p3, end=' -> ')
    p1 = p2
    p2 = p3
    contador += 1
print('Fim')

'''
Exercício feito pelo professor
print('~'*22)
print('SEQUÊNCIA DE FIBONACCI')
print('~'*22)
termos = int(input('Quantos termos você quer mostrar? '))
p1 = 0
p2 = 1
print('~'*30)
print(f'{p1} -> {p2}', end='')
contador = 3
while contador <= termos:
    p3 = p1 + p2
    print(' ->', p3, end='')
    p1 = p2
    p2 = p3
    contador += 1
print(' -> Fim')
print('~'*30)
'''