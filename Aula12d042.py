print('-=-' * 20 )
print('                 Conferidor de Triângulos')
print('-=-' * 20)
r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f'As retas \033[32mpodem\033[m formar um triângulo:')
    if r1 == r2 == r3:
        print('\033[36mEquilátero')
    elif r1 == r2 or r1 == r3 or r2 == r1 or r2 == r3 or r3 == r1 or r3 == r2:
        print('\033[36mIsósceles')
    else:
        print('\033[36mEscaleno\033[m')
else:
    print(f'As retas \033[31mnão podem\033[m formar um triângulo')
