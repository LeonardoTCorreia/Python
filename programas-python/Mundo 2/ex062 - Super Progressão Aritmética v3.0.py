print('='*15)
print('Gerador de PA')
print('='*15)
p = int(input('Primeiro termo: '))
r = int(input('Qual é a razão da PA: '))
contador = 1
soma_termos = 0
while contador <= 10:
    print(p, end=' -> ')
    p += r
    contador += 1
    soma_termos +=1
print('Pausa')
mais_termos = int(input('Você quer mostrar mais quantos termos? '))
while mais_termos != 0:
    contador = 1
    while contador <= mais_termos:
        print(p, end=' -> ')
        p += r
        contador += 1
        soma_termos += 1
    print('Pausa')
    mais_termos = int(input('Você quer mostrar mais quantos termos? '))
print(f'Progressão finalizada com {soma_termos} termos mostrados.')

'''
Exercício feito pelo professor
print('='*15)
print('Gerador de PA')
print('='*15)
p = int(input('Primeiro termo: '))
r = int(input('Qual é a razão da PA: '))
termo = p
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(termo, end=' -> ')
        termo += r
        cont += 1
    print('PAUSA')
    mais = int(input('Você quer mostrar mais quantos termos? '))
print(f'Progressão finalizada com {total} termos mostrados.')
'''