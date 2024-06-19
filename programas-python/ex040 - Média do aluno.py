from time import sleep
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print('Sua média foi {}! Veja sua situação logo abaixo:\n'.format(media))
sleep(2)
print('PROCESSANDO...\n')
sleep(3)
if media < 5:
    print('REPROVADO')
elif 7 > media >=5:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')



