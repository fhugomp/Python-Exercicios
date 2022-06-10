f = ''
while f != 'N':
    s = str(input('\033[36mDigite a letra correspondente ao sexo:[M/F]\033[m ')).strip().upper()
    if s != 'M' and s != 'F':
        print('\033[31mOpção Inválida. Tente novamente.')
    else:
        if s == 'M':
            print(f'\033[34mSexo "{s}" Masculino registrado.')
        else:
            print(f'\033[34mSexo "{s}" Feminino registrado.')
    f = str(input('\033[36mTentar Novamente?[S/N]\033[m ')).strip().upper()
print('Fim da operação')
