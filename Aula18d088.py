# SORTEADOR DE JOGOS DA MEGA-SENA
from random import randint
from time import sleep

jogos = []
temp = []
total = 1
print(f'\033[36m→\033[m' * 35)
p = int(input('\033[34mQuantos jogos você quer? '))
print(f'\033[36m→\033[m' * 35)

while total <= p:
    cont = 0
    while True:
        numsort = randint(1, 60)
        if numsort not in temp:
            temp.append(numsort)
            cont += 1
        if cont >= 6:
            break
    temp.sort()
    total += 1
    jogos.append(temp[:])
    temp.clear()
for i, j in enumerate(jogos):
    print(f'\033[34m{i + 1}º Jogo: {j}')
    sleep(0.75)
print(f'\033[36m{"Boa Sorte!":→^35}')
