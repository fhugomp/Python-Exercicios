# CAIXA ELETRÔNICO
print('\033[36m=' * 20)
print('{:^20}'.format('BANCO FORTALEZA'))
print('=' * 20)
valor = int(input('\033[36mQuanto você quer sacar:R$'))
total = valor
cedatu = 50
totced = 0
print('Você receberá:\033[m')
while True:
    if total >= cedatu:
        total -= cedatu
        totced += 1
    else:
        if totced > 0:
            print(f'\033[34m{totced}\033[m cédulas de \033[32mR${cedatu}')
        if cedatu == 50:
            cedatu = 20
            totced = 0
        elif cedatu == 20:
            cedatu = 10
            totced = 0
        elif cedatu == 10:
            cedatu = 1
            totced = 0
        else:
            break
print('\033[36mVolte Sempre!')
