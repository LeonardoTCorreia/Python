print('{:=^40}'.format(' LOJAS '))
preco = float(input('Preço do produto: R$'))
print('1 - À vista dinheiro/cheque')
print('2 - À vista no cartão')
print('3 - Em até 2x no cartão')
print('4 - 3x ou mais no cartão')
escolha = int(input('Qual é a opção? '))
if escolha == 1:
    desconto = preco - (preco * 0.10)
    print('\nVocê irá pagar o valor com desconto de R${:.2f}'.format(desconto))
elif escolha == 2:
    desconto = preco - (preco * 0.05)
    print('\nVocê irá pagar o valor com desconto de R${:.2f}'.format(desconto))
elif escolha == 3:
    parcelas = preco / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcelas))
    print('Você irá pagar o preço normal de R${:.2f}'.format(preco))
elif escolha == 4:
    juros = preco + (preco * 0.20)
    total_parcelas = int(input('Quantas parcelas? '))
    parcelas = juros / total_parcelas
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(total_parcelas, parcelas))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco, juros))
else:
    print('\nVALOR ERRADO! Reinicie o programa')
