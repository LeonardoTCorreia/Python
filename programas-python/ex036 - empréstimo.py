print('-=-' * 10)
print('Empréstimo bancário')
print('-=-' * 10)
casa = float(input('Qual o valor da casa? R$')) #R$200.000
salario = float(input('Qual o salário do comprador? R$')) #R$1.000
anos = int(input('Em quantos anos você irá pagar a casa? ')) #50 anos
prestacao = casa / (anos * 12)
parcela = salario * 0.30
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(casa, anos, prestacao))
if prestacao > parcela:
    print('Empréstimo negado!\nInfelizmente você não tem crédito suficiente e não poderá comprar essa casa.')
else:
    print('Parabéns, empréstimo CONCEDIDO!!!')
    print('Por mês você irá pagar R${:.2f} em {} anos até completar o valor da casa!'.format(prestacao, anos))
