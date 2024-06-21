resp = 'S'
cont = 1
tot_digitados = soma = maior  = 0
menor = 9999
while resp == 'S':
    n = int(input(f'\nDigite o {cont}º valor: '))
    cont +=1
    soma += n   
    tot_digitados += 1
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    resp = str(input('Quer continuar? [S/N]')).upper().strip() [0]
    if resp not in 'SN':
        print('Dados inválidos, Reinicie o Programa!')
        exit()
media = soma / tot_digitados
print(f'\nVocê digitou {tot_digitados} números e a média foi {media}')
print(f'O maior número digitado foi {maior} e o menor foi {menor}')

'''
Exercício feito pelo professor
resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N]')).upper().strip() [0]
    media = soma / quant
print(f'\nVocê digitou {quant} números e a média foi {media}')
print(f'O maior número digitado foi {maior} e o menor foi {menor}')
'''



