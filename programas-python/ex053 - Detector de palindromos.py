n = str(input('Digite uma frasa para saber se ela é um palíndromo: ')).strip()
new_n = n.lower().replace(' ', '')
reverso = ''.join(reversed(new_n))
if new_n == reverso:
    print('A frase {} é PALÍNDROMO!'.format(reverso))
else:
    print('A frase {} não é PALÍNDROMO!'.format(reverso))

