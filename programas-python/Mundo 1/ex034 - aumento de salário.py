sal = float(input('Digite o valor do seu salário para saber quantos % terá de aumento: R$'))
if sal <= 1250:
    sal_novo = sal + (sal*0.15)
    print('Parabéns, você tem direito a um aumento de 15% no salário!')
    print('Seu salário atual agora é R${:.2f}'.format(sal_novo))
else:
    sal_novo = sal + (sal*0.10)
    print('Parabéns, você tem direito a um aumento de 10% no salário!')
    print('Seu salário atual agora é R${:.2f}'.format(sal_novo))

