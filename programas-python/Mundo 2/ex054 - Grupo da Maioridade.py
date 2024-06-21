from datetime import date
maior = 0
menor = 0
for _ in range(1, 8):
    ano_atual = date.today().year
    nasc = int(input(f'Em que ano a {_}ª nasceu? '))
    idade = ano_atual - nasc
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('{} pessoas já atingiram a maioridade'.format(maior))
print('{} pessoas ainda não atingiram a maioridade'.format(menor))