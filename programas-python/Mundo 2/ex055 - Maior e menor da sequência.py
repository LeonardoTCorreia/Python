maior = 0
menor = 99999
for i in range(1, 6):
    peso = float(input(f'Peso da {i}ª pessoa: '))
    if peso > maior:
        maior = peso
    if i == 0 or peso < menor:
        menor = peso
print('{} foi o maior peso digitado!'.format(maior))
print('{} foi o menor peso digitado!'.format(menor))

'''maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input(f'Peso da {p}ª pessoa: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('{} foi o maior peso digitado!'.format(maior))
print('{} foi o menor peso digitado!'.format(menor))'''