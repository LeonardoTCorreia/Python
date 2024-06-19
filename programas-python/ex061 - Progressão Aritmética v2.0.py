print('='*15)
print('Gerador de PA')
print('='*15)
p = int(input('Digite o primeiro termo da PA: '))
r = int(input('Qual é a razão da PA: '))
contador = 1
while contador <= 10:
    print(p, end=' -> ')
    p += r
    contador += 1
print('Fim')
