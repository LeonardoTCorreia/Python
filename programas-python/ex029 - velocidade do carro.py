velocidade = float(input('Qual a velocidade do seu carro em km/h: '))
if velocidade > 80:
    print('Você ultrapassou o limite de velocidade e está sendo multado!')
    multa = (velocidade - 80) * 7
    print('A multa irá custar R${:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
