def leia_int(txt):
    flag = False
    n = 0
    n = str(input(txt))
    if n.isnumeric():
        print(f'Você digitou {n}. É um numero válido!')
    else:
        print('ERRO! Digite APENAS números.')
        while True:
            n = str(input('Digite um número: ')).strip()
            print('=' * 35)
            if n.isnumeric():
                print(f'Você digitou {n}. É um numero válido!')
                break
            else:
                print('ERRO! Digite APENAS números.')


n = leia_int('Digite um número: ')
print('=' * 35)
