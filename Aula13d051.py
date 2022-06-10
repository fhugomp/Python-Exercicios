pt = int(input('Digite um número: '))
ra = int(input('Digite a razão: '))
d = pt + (11 -1) * ra
for c in range(pt, d, ra):
    print(c, end=' -> ')
print('Fim!')
