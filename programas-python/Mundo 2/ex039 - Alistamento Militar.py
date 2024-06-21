from datetime import date
sexo = input('Qual seu sexo, Masculino ou Feminino? ').lower()
nasc = int(input('Qual a data do seu nascimento? '))
atual = date.today().year
idade = atual - nasc
if sexo == 'masculino':
    if idade < 18:
        saldo = 18 - idade
        print('Você tem {} anos e ainda falta(m) {} ano(s) para se alistar ao serviço militar!'.format(idade, saldo))
        ano = atual + saldo
        print('Seu alistamento será no ano de {}.'.format(ano))
    elif idade == 18:
        print('Você tem {} anos e tem que se alistar IMEDIATAMENTE!'.format(idade))
    elif idade > 18:
        saldo = idade - 18
        print('Você tem {} anos e passou {} ano(s) do tempo de alistamento!'.format(idade, saldo))
        ano = atual - saldo
        print('Seu alistamento foi em {}.'.format(ano))
else:
    print('Você não precisa fazer alistamento militar obrigatório!')


