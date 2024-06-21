print('Descubra seu salário com 15% de aumento meu gafanhoto!!!')
salario = float(input('Qual o salário do funcionário? R$'))
aumento = 0.15 * salario
salario_aumento = salario + aumento
print('O salário com o aumento ficou R${:.2f} reais'.format(salario_aumento))

#ou

print('Descubra seu salário com 15% de aumento meu gafanhoto!!!')
salario = float(input('Qual o salário do funcionário? R$'))
aumento = salario + (salario*15/100)
print('O salário com o aumento ficou R${:.2f} reais'.format(aumento))