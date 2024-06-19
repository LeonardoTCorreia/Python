preco = float(input('Qual o preço do produto? R$'))
desconto = 0.05 * preco
preco_desconto = preco - desconto
print('O valor com desconto de 5% fica no total de R${:.2f}'.format(preco_desconto))

 #ou

preco = float(input('Qual o preço do produto? R$'))
desconto = preco - (preco*5/100)
print('O valor com desconto de 5% fica no total de R${:.2f}'.format(desconto))