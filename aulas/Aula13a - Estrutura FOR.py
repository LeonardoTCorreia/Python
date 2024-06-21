# Usa-se quando sabemos o LIMITE
ini = int(input('início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
for i in range(ini, fim+1, passo): # Na terceira parte da vírgula se eu colocar -1 é igual a contar de trás pra frente; Colocar 2 vai contar de 2 em dois e assim sucessivamente
    print(i)
print('FIM')


s = 0
for c in range(0, 3):
    n = int(input('Digite um número: '))
    s += n
print('O somatório de todos os valores foi {}'.format(s))


