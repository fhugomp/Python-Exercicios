# PROGRAMA DE TABUADA
s = cont = 0
n = int(input('Você quer a tabuada de qual número?: '))
print('-' * 17)
while True:
    cont += 1
    s = n * cont
    print(f'    {n} x {cont} = {s}')
    if cont > 9:
        print('-' * 17)
        n = int(input('Você quer a tabuada de qual número?: '))
        print('-' * 17)
        cont = 0
    if n < 0:
        break
print('Tabuada Encerrada')
print('-' * 17)
