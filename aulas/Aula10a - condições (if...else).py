tempo = int(input('Quantos anos tem seu carro?'))
if tempo <= 3:
    print('Carro novo')
else:
    print('Carro velho')
print('--FIM--')

#ou

tempo = int(input('Quantos anos tem seu carro?'))
print('Carro novo' if tempo <=3 else 'carro velho')
print('--FIM--')

