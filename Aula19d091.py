from random import randint
from time import sleep
from operator import itemgetter

jogadas = {'Jogador 1': randint(1, 6),
           'Jogador 2': randint(1, 6),
           'Jogador 3': randint(1, 6),
           'Jogador 4': randint(1, 6)}
rank = []

print('Os números sorteados foram:')
sleep(0.57)
print('~~' * 13)

for k, v in jogadas.items():
    print(f'{k} tirou {v} no dado.')
    sleep(0.75)

print('~~' * 13)
print('O ranking ficou:')
rank = sorted(jogadas.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(rank):
    print(f'Em {i + 1}º: {v[0]} que tirou {v[1]}')
    sleep(0.75)
