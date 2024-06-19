resp = ()
cont = 1
tot_digitados = 0
soma = 0
while True:
    resp = int(input(f'Digite o {cont}º valor (999 para parar): '))
    cont += 1
    if resp == 999:
        break
    tot_digitados += 1
    soma += resp
print(f'Você digitou {tot_digitados} valores e a soma entre eles foi {soma}.\n')