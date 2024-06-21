s = 0
cont = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        cont += 1
        s += i
print('O somatório de todos os {} valores é {}'.format(cont, s))