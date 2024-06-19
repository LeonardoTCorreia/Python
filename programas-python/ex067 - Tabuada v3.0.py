n = 1
cont = 1
result = 0
while n >= 0:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*30)
    cont = 1
    if n < 0:
        print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
        break
    while cont <= 10:
        result = n * cont
        print(f'{n} x {cont} = {result}')
        cont += 1
    print('-'*30)
    
