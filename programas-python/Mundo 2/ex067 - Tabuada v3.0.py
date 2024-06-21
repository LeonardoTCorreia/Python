while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*30)
    cont = 1
    if n < 0:        
        break
    while cont <= 10:
        print(f'{n} x {cont} = {n*cont}')
        cont += 1
    print('-'*30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!\n')  
