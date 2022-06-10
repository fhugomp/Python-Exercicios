# Jogando Par ou Impar
from random import randint
print('=' * 25)
print('VAMOS JOGAR \033[32mPAR\033[m OU \033[33mIMPAR\033[m!')
print('=' * 25)
vit = 0
while True:
    pces = randint(0, 11)
    jesn = int(input('Digite um número: '))
    jes = str(input('[I/P]:')).strip().upper()[0]
    print(f'Você digitou: {jesn} e o Computador: {pces}')
    soma = jesn + pces
    if soma % 2 == 0:
        print('Deu \033[32mPAR!\033[m', end='')
        if jes == 'P':
            print(' Você \033[34mGANHOU\033[m')
            print('=' * 25)
            print('\033[36mVamos De Novo\033[m')
            vit += 1
        else:
            print(' Você \033[31mPERDEU\033[m')
            break
    else:
        print('Deu \033[33mIMPAR!\033[m', end='')
        if jes == 'I':
            print(' Você \033[34mGANHOU\033[m')
            print('=' * 25)
            print('\033[36mVamos De Novo\033[m')
            vit += 1
        else:
            print(' Você \033[31mPERDEU\033[m')
            break
print(f'Você ganhou {vit} veze(s)')
