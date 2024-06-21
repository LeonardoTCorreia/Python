print('{:=^40}'.format(' TABUADA '))
n = int(input('\nDigite um número inteiro para ver a sua tabuada: '))
print('-' * 15)
for i in range(1, 21):
    result = n * i
    print('{} X {:2} = {}'.format(n, i, result))
print('-' * 15)


