cid = str(input('Digite o nome de uma cidade: '))
print(cid[:5].upper() == 'SANTO')

# errado cidade = str(input('Digite o nome de uma cidade: ')).strip()
dividido = cidade.upper().split()
print('Santo' in dividido[0])



