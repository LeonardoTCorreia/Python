resp = ()
cont = 1
tot_digitados = 0
soma = 0
while resp != 999:
    resp = int(input(f'Digite o {cont}º valor: '))
    cont += 1
    if resp != 999:
        tot_digitados += 1
        soma = soma + resp
    else:
        print('')
print(f'Você digitou {tot_digitados} valores e a soma entre eles foi {soma}.\n')

'''
Outra solução
num = cont = soma = 0
while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    soma += num
    cont += 1
print(f'Você digitou {cont - 1} valores e a soma entre eles foi {soma - 999}.\n')
'''
'''
Mais uma solução
num = cont = soma = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para parar]: '))
print(f'Você digitou {cont} valores e a soma entre eles foi {soma}.\n')
'''
