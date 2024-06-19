print('\nDigite um valor em metros para descobrir seu valor em centímetros e milímetros!\n')
metros = int(input('Uma distância em metros: '))
km = metros /1000
hm = metros /100
dam = metros / 10
dm = metros * 10
cent = metros * 100
mili = metros * 1000
print('A medida de {}m corresponde a\n'.format(metros))
print('{}km\n{}hm\n{}dam\n{}dm\n{}cm\n{}mm'.format(km, hm, dam, dm, cent, mili))
