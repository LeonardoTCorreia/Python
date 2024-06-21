print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)
p = int(input('Digite o primeiro termo da PA: '))
r = int(input('Qual é a razão da PA: '))
decimo = p + (10-1) * r
for i in range(p, decimo+r, r):
    print(i, end=' -> ')
print('FIM')