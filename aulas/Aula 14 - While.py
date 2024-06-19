# # Usa-se quando sabemos o LIMITE e tbm quando NÃO SABEMOS
n = 1
par = impar = 0
while n != 0:
    n = int(input("Digite um valor: "))
    if n !=0:
        if n % 2 == 0:
            par +=1
        else:
            impar +=1
print(f'Você digitou {par} números pares e {impar} números ímpares!')

'''r = 'S'
while r == 'S':
    n = int(input("Digite um número: "))
    r = str(input("Quer continuar? [S/N]")).upper()
print('FIM')'''

'''c = 1
while c < 10:
    print(c)
    c += 1
print('Fim')'''