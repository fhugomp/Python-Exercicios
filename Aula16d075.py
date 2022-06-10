# LENDO 4 NÚMEROS E MOSTRANDO: QUANTOS 9 APARECERAM, SE O NÚMERO 3 APARECEU E SUA POSIÇÃO E QUAIS OS NÚMEROS PARES.
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))
n = n1, n2, n3, n4
print(f'\n\033[36mO número 9 apareceu {n.count(9)} vezes.')
if 3 in n:
    print(f'O número 3 apareceu pela primeira vez na {n.index(3)+ 1}ª posição.')
else:
    print(f'Não teve nenhum número 3.')
print('os números pares foram: ', end='')
for e in n:
    if e % 2 == 0:
        print(f'{e}', end=', ')
