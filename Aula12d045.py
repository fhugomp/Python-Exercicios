from random import choice
print('\033[31mIae, acha que é bom o bastante pra me vencer em uma partida de jokenpô?\033[m')
print('[T] \033[34mTesoura')
print('[P] \033[32mPapel')
print('[R] \033[35mPedra')
escolha = str(input('\n\033[36mEscolha e digite uma das letras acima pra jogar:\033[m  ')).strip().lower()
escolhapc = ['r' , 'p' , 't']
escolhapc1 = choice(escolhapc)
if escolha == 't' and escolhapc1 == 'r':
    print('-=' * 18)
    print(f'\033[31mHaha você escolheu Tesoura, EU GANHEI! GG\033[m')
    print('-=' * 18)
elif escolha == 't' and escolhapc1 == 'p':
    print('-=' * 18)
    print('\033[32mDroga! Escolhi papel. Parece que VOCÊ GANHOU, GG\033[m')
    print('-=' * 18)
elif escolha == 'p' and escolhapc1 == 't':
    print('-=' * 18)
    print(f'\033[31mHaha você escolheu Papel, EU GANHEI! GG\033[m')
    print('-=' * 18)
elif escolha == 'p' and escolhapc1 == 'r':
    print('-=' * 18)
    print('\033[32mDroga! Escolhi pedra. Parece que VOCÊ GANHOU, GG.')
    print('-=' * 18)
elif escolha == 'r' and escolhapc1 == 't':
    print('-=' * 18)
    print('\033[32mDroga! Escolhi Tesoura. Parece que VOCÊ GANHOU, GG')
    print('-=' * 18)
elif escolha == 'r' and escolhapc1 == 'p':
    print('-=' * 18)
    print(f'\033[31mHaha você escolheu Pedra, EU GANHEI! GG\033[m')
    print('-=' * 18)
else:
    print('-=' * 18)
    print('\033[35mParece que foi EMPATE, GG\033[m')
    print('-=' * 18)
