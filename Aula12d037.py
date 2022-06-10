num = int(input('Digite um numéro: '))
print('[1] \033[33mBinário\033[m')
print('[2] \033[33mOctal\033[m')
print('[3] \033[33mHexadecimal\033[m')
print('[0] \033[31mCancelar\033[m')
pernum = str(input('Digite umas das opções acima para a qual você deseja converter:\n')).strip()
if pernum == '0':
    print('\033[31mOperação Cancelada\033[m')
elif pernum == '1' or pernum == '2' or pernum == '3':
    if pernum == '1':
        # bina = str(bin(num))  # Comando pra transformar em Binário
        print(f'\033[36mA sua conversão é: {bin(num)[2:]}')
    elif pernum == '2':
        # octa = str(oct(num))  # Comando para transformar em Octal
        print(f'\033[36mA sua conversão é: {oct(num)[2:]}')
    elif pernum == '3':
        # hexag = str(hex(num))  # Comando pra transformar em Hexadecimal
        print(f'\033[36mA sua converção é: {hex(num)[2:]}')
else:
    print('Opção invalida')