print('-=-' * 20)
print('Analisador de Triângulos')
print('-=-' * 20)
r1 = float(input('Digite o comprimento da 1ª reta: '))
r2 = float(input('Digite o comprimento da 2ª reta: '))
r3 = float(input('Digite o comprimento da 3ª reta: '))
if (r1 + r2) > r3 and (r1 + r3) > r2 and (r2 + r3) > r1:
    if r1 == r2 == r3:
        print('Essas retas podem formar um triângulo!\nO tipo é EQUILÁTERO')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Essas retas podem formar um triângulo!\nO tipo é ISÓSCELES')
    else:
        print('Essas retas podem formar um triângulo!\nO tipo é ESCALENO')
else:
    print('Essas retas não podem formar um triângulo, tente novamente!')