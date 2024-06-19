n = int(input('Digite um número inteiro para ver sua tabuada: '))
for i in range(1, 11):
    print('{} X {:2} = {}'.format(n, i, n*i))
print('FIM')