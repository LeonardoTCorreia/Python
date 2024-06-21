n = int(input('Digite um número para saber se ele é primo: '))
tot = 0
for i in range(1, n + 1):
    if n % i == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print(f'{i} ', end='')
print(f'\n\033[mO número {n} foi divisível {tot} vezes')
if tot == 2:
    print(f'\n{n} é PRIMO')
else:
    print(f'\n{n} NÃO É PRIMO')

'''primo = n % 1 == 0 and n % n == 0
if n == primo:
    print('É um número PRIMO')
else:
    print('Esse número não é PRIMO')'''