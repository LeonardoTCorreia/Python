n = int(input('Digite um número para calcular seu fatorial: '))
n_old = n
result = 1
print(f'Calculando {n_old}! = ', end='')
while n > 0:
    result *= n
    if n <= 1:
        print(f'{n}', end='' f' = {result}')
    else:
        print(f'{n}', end=' x ')
    n -= 1

'''Exercício feito pelo professor
n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 
    else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')'''

''' Resolução com biblioteca
from math import factorial
n= int(input('Digite um número para calcular o seu Fatorial: '))
f = factorial(n)
print('O fatorial de {n} é {f}')
'''

