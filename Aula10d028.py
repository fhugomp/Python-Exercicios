from random import randint
from time import sleep
n = randint(0 , 5)
print('-=-' * 20)
print('Vou pensar em um número de 0 a 5 e você tenta advinhar ok?')
print('-=-' * 20)
usu = int(input('Digite um número inteiro de 0 a 5: '))
print('Processando...')
sleep(1)
if usu == n:
    print(f'Parebéns, você acertou o número que eu pensei foi: {n}')
else:
    print(f'Você errou, o número que eu pensei foi: {n}')
print('----Fim----')
