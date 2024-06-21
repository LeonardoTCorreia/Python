def estatisticas_produtos ():
    print('-'*30)
    print('LOJA SUPER BARATÃO')
    print('-'*30)

    tot_compra = mais_1000 = preco_barato = cont = 0
    nome_barato = ''
    while True:
        nome_produto = str(input('Nome do Produto: ')).strip()
        preco = float(input('Preço: R$'))
        tot_compra += preco
        cont += 1
        if preco > 1000:
            mais_1000 += 1
        if cont == 1 or preco < preco_barato:
            preco_barato = preco
            nome_barato = nome_produto
        print('-'*30)
        resposta = ' '
        while resposta not in 'SN':
                resposta = str(input('Quer continuar? [S/N] ')).upper().strip() [0]
        print('-'*30)
        if resposta == 'N':
            break
    print(f'O total da compra foi R${tot_compra}')
    print(f'Temos {mais_1000} produtos custando mais de R$1000.00')
    print(f'O produto mais barato foi {nome_barato} que custa R${preco_barato:.2f}')
            
estatisticas_produtos()