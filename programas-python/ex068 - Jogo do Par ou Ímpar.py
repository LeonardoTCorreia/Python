from random import randint

def jogar_par_ou_impar():
    print('=-'*20)
    print('VAMOS JOGAR PAR OU ÍMPAR')
    print('-='*20)

    cont_venceu = 0

    while True:
        jog = int(input('Digite um valor: '))
        comp = randint(0, 10)
        escolha_jogador = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
        soma = jog + comp
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

print("\nObrigado por jogar! Até a próxima!")

'''def jogar_par_ou_impar():
    print('=-'*20)
    print('VAMOS JOGAR PAR OU ÍMPAR')
    print('-='*20)
    cont_venceu = 0
    while True:
        jog = int(input('Digite um valor: '))
        comp = randint(0, 10)
        
        escolha_jogador = ''
       # escolha_jogador = str(input('Par ou Ímpar? [P/I] ')).upper().strip() [0]
        while escolha_jogador not in 'PI':
            escolha_jogador = str(input('Par ou Ímpar? [P/I] ')).upper().strip() [0]
            if escolha_jogador not in 'PI':
                print('Jogada inválida. Tente novamente!')
        
        soma = jog + comp
        if soma % 2 == 0:
            result = 'P'
        else:
            result = 'I'
        print('-'*40)
        
        print(f'Você jogou {jog} e o computador {comp}. Total de {soma} ', end='')
        
        if escolha_jogador == result:
            print(f'deu PAR' if result == 'P' else 'deu ÍMPAR')
            print('-'*40)
            print('Você VENCEU!!!')
            print('Vamos jogar novamente...')
            print('-='*20)
            cont_venceu += 1         
        else:
            print(f'deu PAR' if result == 'P' else 'deu ÍMPAR')
            print('-'*40)
            print('Você PERDEU!')
            break
    
    print('-='*20)
    print(f'GAME OVER! Você venceu {cont_venceu} vezes.')

while True:
    jogar_par_ou_impar()

    resposta = str(input('Deseja jogar novamente? [S/N] ')).upper().strip() [0]
    if resposta != 'S':
            break
        
print('Obrigado por jogar! Até a próxima!')'''

