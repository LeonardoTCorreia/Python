frase = str(input('Digite uma frase: ')).lower().strip()
print('A letra "a" aparece no total de:', frase.count('a'), 'vezes')
print('Apareceu pela 1ª vez na posição:', frase.find('a') + 1)
print('Apareceu pela última vez na posição:', frase.rfind('a') + 1)

