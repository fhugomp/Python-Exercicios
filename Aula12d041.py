from datetime import date
ano = int(input('Digite o ano de nascimento: '))
idade = date.today().year - ano
print(f'Quem nasceu em: {ano} tem {idade} ano(s)')
if idade <= 9:          # Mirim
    print(f'{idade} anos, categoria "Mirim".')
elif 15 > idade > 9:    # Infantil
    print(f'{idade} anos, categoria "Infantil"')
elif 20 > idade > 14:   # Junior
    print(f'{idade} anos, categoria "Junior".')
elif idade == 20:       # Sênior
    print(f'{idade} anos, categoria "Sênior".')
else:                   # Master
    print(f'{idade} anos, categoria "Master".')
