from time import sleep
per = ''
n1 = int(input('\033[36mDigite um número: '))
n2 = int(input('\033[36mDigite outro número: \033[m'))
while per in '12345':
    print('    \033[34m[1] Somar\033[m')
    print('    \033[33m[2] Multiplicar\033[m')
    print('    \033[35m[3] Maior Número\033[m')
    print('    \033[32m[4] Digitar Novamente\033[m')
    print('    \033[31m[5] Sair do programa\033[m')
    per = str(input('\033[36m>>>Digite umas das opções acima: \33[m'))
    if per == '1':
        print(f'\033[34mA soma de "{n1}" e "{n2}" é: {n1 + n2}.')
    if per == '2':
        print(f'\033[33mO resultado da multiplicação entre "{n1}" e "{n2}" é: {n1 * n2}.')
    if per == '3':
        if n1 > n2:
            print(f'\033[35mO "{n1}" é MAIOR que o "{n2}".')
        if n1 < n2:
            print(f'\033[35mO "{n2}" é MAIOR que o "{n1}".')
        else:
            print('\033[35mOs dois valores são IGUAIS.')
    if per == '4':
        n1 = int(input('\033[36mDigite um número: '))
        n2 = int(input('Digite outro número: \033[m'))
    if per == '5':
        print('\033[36mFinalizando...')
        sleep(2.5)
        print('\033[36mOperação Finalizada')
        break
    if per > '5':
        print('\033[31mOpção Inválida. Tente Novamente')
    print('\033[36m=#=' * 18)
    sleep(3)