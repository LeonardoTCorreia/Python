import math
cat_opo = float(input('Digite o cateto oposto do triângulo retângulo: '))
cat_adj = float(input('Digite o cateto adjacente do triângulo retângulo: '))
hip = math.hypot(cat_opo, cat_adj)
print('O comprimento da hipotenusa é {:.2f}'.format(hip))

'''cat_opo = float(input('Digite o cateto oposto do triângulo retângulo: '))
cat_adj = float(input('Digite o cateto adjacente do triângulo retângulo: '))
hip = (cat_opo ** 2 + cat_adj ** 2) ** (1/2)
print('O comprimento da hipotenusa é {:.2f}'.format(hip))'''