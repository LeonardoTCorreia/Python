from random import randint
from time import sleep
print('-=-'*10)
print('JOKENPÔ')
print('-=-'*10)
lista = ['Pedra', 'Papel', 'Tesoura']

print('0 - Pedra')
print('1 - Papel')
print('2 - Tesoura')

computador = randint(0, 2)

jogador = int(input('Qual é sua jogada?: '))
if jogador != 0 and jogador != 1 and jogador != 2:
    print('Jogada INVÁLIDA!')
    exit()
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=-'*15)
print('Computador jogou {}'.format(lista[computador]))
print('Jogador jogou {}'.format(lista[jogador]))
print('-=-'*15)

if computador == jogador:
    print('EMPATE')
elif computador == 0:#pedra
    if jogador == 1:
        print('Jogador Venceu!!!')
    elif jogador == 2:
        print('Computador Venceu!!!')
    else:
        print('Jogada INVÁLIDA!')
elif computador == 1: # papel
    if jogador == 0:#pedra
        print('Computador Venceu!!!')
    elif jogador == 2:#tesoura
        print('Jogador Venceu!!!')
    else:
        print('Jogada INVÁLIDA!')
elif computador == 2: # tesoura
    if jogador == 0:#pedra
        print('Jogador Venceu!!!')
    elif jogador == 1:#papel
        print('Computador Venceu!!!')
    else:
        print('Jogada INVÁLIDA!')





