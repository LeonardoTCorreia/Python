print ('Saiba o sucessor e o antecessor de qualquer número inteiro!\n')
n = int(input('Digite um número inteiro: '))
suc = n + 1
ant = n - 1
print('O sucessor de {} é {}'.format(n, suc))
print('O antecessor de {} é {}'.format(n, ant))

#OU

print ('Saiba o sucessor e o antecessor de qualquer número inteiro!\n')
n = int(input('Digite um número inteiro: '))
print('O sucessor de {} é {}'.format(n, (n+1)))
print('O antecessor de {} é {}'.format(n, (n-1)))
