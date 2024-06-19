print('-=-' * 20)
print('Analisador de Triângulos')
print('-=-' * 20)
r1 = float(input('Digite o comprimento da 1ª reta: '))
r2 = float(input('Digite o comprimento da 2ª reta: '))
r3 = float(input('Digite o comprimento da 3ª reta: '))
if (r1 + r2) > r3 and (r1 + r3) > r2 and (r2 + r3) > r1:
    print('Parabéns, essas retas podem formar um triângulo!')
else:
    print('Essas retas não podem formar um triângulo, tente novamente!')