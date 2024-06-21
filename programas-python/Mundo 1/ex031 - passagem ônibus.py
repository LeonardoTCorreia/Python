km = float(input('Qual a distância de uma viagem em km? '))
#preco = km * 0.50 if km <= 200 else km * 0.45
if km <= 200:
    preco = km * 0.50
else:
    preco = km * 0.45
print('Você rodou {}km e irá pagar um total de R${:.2f}'.format(km, preco))
