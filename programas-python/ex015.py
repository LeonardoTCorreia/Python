print('=' * 10, 'Aluguel de carros', '=' * 10)
dias = int(input('Quantos dias alugados?'))
km = float(input('Quaantos Km rodados?'))
preco_pagar = dias * 60
km_rodado = km * 0.15
total = preco_pagar + km_rodado
print('O total a pagar é de R${:.2f}'.format(total))

#ou

print('=' * 10, 'Aluguel de carros', '=' * 10)
dias = int(input('Quantos dias alugados?'))
km = float(input('Quaantos Km rodados?'))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(total))
