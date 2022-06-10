from time import sleep
print('Iniciando o lançamento do foguete. O lançamento vai ocorrer em:')
sleep(1)
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('\033[34mFoguete lançado!!!')
