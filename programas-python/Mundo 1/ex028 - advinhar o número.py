import random
from time import sleep
r = random.randint(0, 5) # computador pensando
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...') # usuário tentando adivinhar
print('-=-' * 20)

n = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if n == r:
    print('\nParabéns, você acertou!')
else:
    print('\nO computador venceu :(')
print('\nEle havia pensado no número {}.'.format(r))

