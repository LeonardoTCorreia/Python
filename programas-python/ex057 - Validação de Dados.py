sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('\nInforme seu sexo: [M/F] ')).strip().upper() [0] #[0] = apenas pegar a primeira letra
    if sexo == 'M':
        print('\nSexo M registrado com sucesso')
    elif sexo == 'F':
        print('\nSexo F registrado com sucesso')
    else:
        print('\nDados inválidos, você tem apenas duas opções [M/F]!\nTente Novamente!')

# Outra forma de fazer esse exercício

'''sexo = str(input('\nInforme seu sexo: [M/F] ')).strip().upper() [0] #[0] = apenas pegar a primeira letra
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper() [0]
print(f'Sexo {sexo} registrado com sucesso')'''

