def leia_int(txt):
    while True:
        try:
            n = int(input(txt))
        except (ValueError, TypeError):
            print('\033[1:31mERRO! Digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[1:31mInfelizmento o usuário decidiu interromper a operação.\033[m')
            return 0
        else:
            return n


def leia_float(txt):
    while True:
        try:
            n = float(input(txt))
        except (ValueError, TypeError):
            print('\033[1:31mERRO! Digite um número real válido\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[1:31mInfelizmento o usuário interrompeu a operação.\033[m')
            return 0
        else:
            return n


try:
    nint = leia_int('Digite um número inteiro: ')
    nfloat = leia_float('Digite um número real: ')
except KeyboardInterrupt:
    print('\033[1:31mInfelizmento o usuário interrompeu a operação.\033[m')
print(f'Você digitou os valores {nint} e {nfloat}')
