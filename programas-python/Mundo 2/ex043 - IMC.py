print('-=-' * 10)
print('Descubra seu IMC!!!')
print('-=-' * 10)
peso = float(input('Qual seu peso? (ex: 85.45) '))
altura = float(input('Qual a sua altura? (ex: 1.78) '))
imc = peso / (altura**2)
print('\nSeu IMC é {:.2f} e você está no status: '.format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc <25:
    print('Peso ideal')
elif imc >= 25 and imc < 30:
    print('Sobrepeso')
elif imc >= 30 and imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')
