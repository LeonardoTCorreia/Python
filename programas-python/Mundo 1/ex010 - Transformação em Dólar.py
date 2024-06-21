print('Fala o din que você tem na carteira que vamos dizer quantos dólares você pode comprar!\n')
real = float(input('Quantos reais você tem na carteira meu jovem ou minha jovem? R$'))
dolar = real / 5.18
euro = real / 5.54
print('\nCom R${:.2f}, você pode comprar US${:.2f}.\nCom R${:.2f}, você pode comprar E${:.2f}.'.format(real, dolar, real, euro))
