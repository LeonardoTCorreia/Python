from time import sleep
n1 = int(input('Digite o 1º valor: '))
n2 = int(input('Digite o 2º valor: '))
maior = n1
while n1 != 0 and n2 != 0:
    print('''\n[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa''')
    escolha = int(input(('\n>>>> Escolha uma das opções acima: ')))
    if escolha == 1:
        soma = n1 + n2
        print(f'A soma de {n1} e {n2} é {soma}.')
    elif escolha == 2:
        mult = n1 * n2
        print(f'A multiplicação de {n1} x {n2} é {mult}.')
    elif escolha == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2}, o maior número digitado foi {maior}.')
    elif escolha == 4:
        print('Informe os números novamente:')
        n1 = float(input('Digite o 1º valor: '))
        n2 = float(input('Digite o 2º valor: '))
    elif escolha == 5:
        print('\nFim do programa!')
        exit()
    else:
        print('Escolha errada. Tente Novamente!')
    print('=-=' * 10)
    sleep(1.4)