from datetime import date
ano = int(input('Qual o ano de nascimento do atleta? '))
idade = date.today().year - ano
print('Você tem {} anos e sua categoria é: '.format(idade))
if idade < 10:
    print('MIRIM!')
elif idade < 15:
    print('INFANTIL!')
elif idade < 20:
    print('JUNIOR!')
elif idade < 26:
    print('SÊNIOR!')
else:
    print('MASTER!')
