# GERANDO 5 NÚMEROS ALÉATORIOS E DIZENDO QUAL É O MAIOR E QUAL É O MENOR
from random import randint
na = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print('Números aléatorios: ', end='')
for n in na:
    print(f'{n}, ', end='')
print(f'\nO maior número é: {max(na)}')
print(f'O menor número é: {min(na)}')
