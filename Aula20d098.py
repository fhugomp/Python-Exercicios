from time import sleep


def contador(i, f, p):
    print('~' * 45)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    print('~' * 45)
    sleep(2)
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i > f:
        for c in range(i, f - 1, -p):
            print(f'{c} → ', end='')
            sleep(0.35)
        print('FIM')
    else:
        for c in range(i, f + 1, p):
            print(f'{c} → ', end='')
            sleep(0.35)
        print('FIM')


#  Programa Principal
contador(1, 10, 1)
contador(10, 0, -2)
print('~' * 45)
print('Agora é a sua vez! Escolha o:')
ini = int(input('Inicio: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)
