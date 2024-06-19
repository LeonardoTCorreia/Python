import random
from time import sleep
comp = random.randint(0, 10) # computador pensando
print('Sou seu computador...')
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...') # usuário tentando adivinhar
print('-=-' * 20)
jog = ()
cont = 0
while jog != comp:
    jog = int(input('Em que número eu pensei? '))
    print('\nPROCESSANDO...\n')
    sleep(0.5)
    if jog == comp:
        print('Parabéns, você acertou!')
    else:
        if jog > comp:
            print('Menos... Tente outra vez.')
        else:
            print('Mais... Tente outra vez.')    
    cont += 1
print(f'Você fez {cont} tentativas até acertar!')
print(f'O computador havia pensado no número {comp}.\n')

'''Exercício feito pelo professor
from random import randint
comp = randint (0, 10)
print('Sou seu computador...')
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...') # usuário tentando adivinhar
print('-=-' * 20)
acertou = False
palpites = 0
while not acertou:
    jog = int(input('Em que número eu pensei? '))
    palpites += 1
    if jog == comp:
        acertou = True
    else:
        if jog < comp:
            print('Mais... Tente outra vez.')
        else:
            print('Menos... Tente outra vez.')
print(f'Você fez {palpites} tentativas até acertar!')
print(f'O computador havia pensado no número {comp}.') '''      



