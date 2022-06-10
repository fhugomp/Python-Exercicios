print('-=-' * 20)
print('                 Conferidor de Triângulos')
print('-=-' * 20)
r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f'Os seguimentos digitados PODEM formar um triângulo.')
else:
    print('Os seguimentos digitados NÃO PODEM formar um triângulo.')
