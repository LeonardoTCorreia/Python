def dados_grupo ():
    print ('-'*20)
    print('CADASTRE UMA PESSOA')
    print ('-'*20)

    mais_18 = tot_homens = mulher_menos_20 = 0

    while True:
        idade = int(input('Idade: '))
        sexo = ' '
        while sexo not in 'MF':
            sexo = str(input('Sexo: [M/F]')).upper().strip() [0]
        if idade >= 18:
            mais_18 += 1
        if sexo == 'M':
            tot_homens += 1
        if sexo == 'F' and idade < 20:
            mulher_menos_20 += 1
        print ('-'*20)
        resposta = ' '
        while resposta not in 'SN':
            resposta = str(input('Quer continuar? [S/N] ')).upper().strip() [0]
        print ('-'*20)

        if resposta == 'N':
            break
    print('===== FIM DO PROGRAMA =====')
    print(f'\nTotal de pessoas com mais de 18 anos: {mais_18}')
    print(f'Ao todo temos {tot_homens} homens cadastrados')
    print(f'E temos {mulher_menos_20} mulheres com menos de 20 anos')
            
dados_grupo()