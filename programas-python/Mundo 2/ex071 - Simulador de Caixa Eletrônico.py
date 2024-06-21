import random
def caixa_eletronico ():
    print('=-'*15)
    print('{:^30}'.format('BANCO LTC'))
    print('-='*15)
    valor = int(input('Qual valor você quer sacar? R$'))
    total = valor
    cedula = 50
    tot_cedula = 0
    while True:
        if total >= cedula:
            total -= cedula
            tot_cedula += 1
        else:
            if tot_cedula > 0:
                print(f'Total de {tot_cedula} cédulas de R$ {cedula}')
            if cedula == 50:
                cedula = 20
            elif cedula == 20:
                cedula = 10
            elif cedula == 10:
                cedula = 1
            tot_cedula = 0
            if total == 0:
                break
    print('=-'*15)
    print('Volte sempre ao BANCO LTC! Tenha um bom dia!')
caixa_eletronico()
