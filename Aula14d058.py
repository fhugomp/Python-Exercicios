from random import randint
cont = 0
tm = randint(0, 10)
tj = 0
print('\033[34mVou pensar em um número de 0 à 10 e você tenta advinhar, ok?\033[m')
while tj != tm:
    tj = int(input('\033[34mDigita um número: '))
    cont += 1
    if tj != tm:
        print('\033[31mErrou!')
        if tj > tm:
            print('\033[33mO meu número é Menor que esse.')
        else:
            print('\033[32mO meu número é Maior que esse.')
print('\033[36mParabéns! Você acertou.')
print(f'Você precisou de {cont} chances para acertar.')
