nome = str(input('Digite seu nome completo: ')).strip()
name = nome.split()
print(nome)
print('\nPrimeiro: ', name[0])
print('\nÚltimo: {}'.format(name[len(name)-1]))
