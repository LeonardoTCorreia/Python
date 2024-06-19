s = 0
c = 1
for i in range(1, 7):
    n = int(input("Digite o {} número: ".format(c)))
    if n % 2 == 0:
        s += n
        c += 1
print(f'A soma total contabilizando apenas os números pares foi {s}')