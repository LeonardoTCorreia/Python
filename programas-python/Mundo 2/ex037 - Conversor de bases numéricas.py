num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
converter = int(input('Sua opção: '))
if converter == 1:
    print('{} convertido para binario é igual a {}'.format(num, bin(num)[2:]))
elif converter == 2:
    print('{} convertido para octal é igual a {}'.format(num, oct(num)[2:]))
elif converter == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Ops, valor errado, reinicie o programa!')
