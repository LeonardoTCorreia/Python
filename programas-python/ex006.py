print('Digite um número inteiro para saber seu dobro, triplo e raiz quadrada!')
n = int(input('Digite um número: '))
dobro = n * 2
triplo = n * 3
raiz = n**(1/2)
print('O dobro de {} é {}.'.format(n, dobro))
print('O triplo de {} é {}.'.format(n, triplo))
print('A raiz quadrada de {} é {:.2f}.'.format(n, raiz))

#OU

print('Digite um número inteiro para saber seu dobro, triplo e raiz quadrada!')
n = int(input('Digite um número: '))
print('O dobro de {} é {}.'.format(n, (n * 2)))
print('O triplo de {} é {}.'.format(n, (n* 3)))
print('A raiz quadrada de {} é {:.2f}.'.format(n, pow(n, (1/2))))