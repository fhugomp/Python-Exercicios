n = int(input('Digite um número: '))
if 10 <= n:
    print('\033[36mSó são aceitos valores de 1 à 9. Tente novamente.')
else:
    print(f'\033[31m{"TABUADA":=^11}')
    for c in range(1, 11):
        cont = c
        s = c * n
        print(f'{n} x {cont} = {s}')
    print('\033[31m=' * 11)
