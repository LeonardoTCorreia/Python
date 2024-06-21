n1 = int(input('Digite o nº 1: '))
n2 = int(input('Digite o nº 2: '))
n3 = int(input('Digite o nº 3: '))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))

'''if n1 > n2 and n1 > n3:
    print('{} é o maior número'.format(n1))
elif n2 > n1 and n2 > n3:
    print('{} é o maior número'.format(n2))
else:
    print('{} é o maior número'.format(n3))

if n1 < n2 and n1 < n3:
    print('{} é o menor número'.format(n1))
elif n2 < n1 and n2 < n3:
    print('{} é o menor número'.format(n2))
else:
    print('{} é o menor número'.format(n3))'''
