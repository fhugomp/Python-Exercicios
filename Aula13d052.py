n = int(input('Digite um número: '))
for c in range(1, 548):
    pr = n // c
if pr == 0 and n // n == 0:
    print(f'O número {n} \033[34m é um número primo.')
elif n > 548:
    print(f'Digite \033[33msomente\033[m números de 1 à 548 ')
else:
    print(f'O número {n}\033[31m não é\033[m um número primo.')
