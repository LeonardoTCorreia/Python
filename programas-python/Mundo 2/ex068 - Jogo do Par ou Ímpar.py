from random import randint

def jogar_par_ou_impar():
    print('=-'*20)
    print('VAMOS JOGAR PAR OU ÍMPAR')
    print('-='*20)

    cont_venceu = 0

    while True:
        jog = int(input('Digite um valor: '))
        comp = randint(0, 10)
        soma = jog + comp
        escolha_jogador = ' '
        while escolha_jogador not in 'PI':
            escolha_jogador = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
        if soma % 2 == 0:
            result = 'P'
        else:
            result = 'I'
        print('-'*40)
        print(f'Você jogou {jog} e o computador {comp}. Total de {soma} ', end='')
        
        if escolha_jogador == result:
            print('deu PAR' if result == 'P' else 'deu ÍMPAR')
            print('-'*40)
            print('Você VENCEU!!!')
            print('Vamos jogar novamente...')
            print('-='*20)
            cont_venceu += 1        
        else:
            print('deu PAR' if result == 'P' else 'deu ÍMPAR')
            print('-'*40)
            print('Você PERDEU!')
            break
    print('-='*20)
    print(f'GAME OVER! Você venceu {cont_venceu} vezes.')

while True:
    jogar_par_ou_impar()
    resposta = input("Deseja jogar novamente? [S/N] ").upper().strip()
    if resposta != 'S':
        break
print("\nObrigado por jogar! Até a próxima!\n")
'''
Exercício feito pelo professor
from random import randint

print('=-'*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-='*20)
cont_venceu = 0
while True:
    jog = int(input('Digite um valor: '))
    comp = randint(0, 10)
    soma = jog + comp
    escolha_jogador = ' '
    while escolha_jogador not in 'PI':
        escolha_jogador = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    print(f'Você jogou {jog} e o computador {comp}. Total de {soma} ', end='')
    print('DEU PAR' if soma % 2 == 0 else 'DEU ÍMPAR')
    if escolha_jogador == 'P':
        if soma % 2 == 0:
            print('Você VENCEU!')
            cont_venceu += 1
        else:
            print('Você PERDEU!')
            break
    elif escolha_jogador == 'I':
        if soma % 2 == 1:
            print('Você VENCEU!')
            cont_venceu += 1
        else:
            print('Você PERDEU!')
            break
    print('-'*40)
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {cont_venceu} vezes.')
'''


