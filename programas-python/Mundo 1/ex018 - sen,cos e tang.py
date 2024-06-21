import math
ang = int(input('Digite um ângulo: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))
print('\nVamos mostrar o seno, cosseno e a tangente do ângulo {}°'.format(ang))
print('\nSeno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}'.format(sen, cos, tang))
