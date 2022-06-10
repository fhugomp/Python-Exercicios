cont = 1
ter = int(input('Digite o primeira termo: '))
ra = int(input('Digite a razão: '))
termo = ter
while cont <= 10:
    print(f'{termo} -> ', end='')
    termo += ra
    cont += 1
print('Fim')
