maiorp = 0
menorp = 0
for p in range(1, 6):
    peso = float(input(f'Digite o {p}º peso: '))
    if p == 1:
        maiorp = peso
        menorp = peso
    else:
        if peso > maiorp:
            maiorp = peso
        if peso < menorp:
            menorp = peso
print(f'\nDo total de pesos lidos \nA pessoa com maior peso foi: {maiorp}Kg'
      f'\nE a menor foi: {menorp}Kg.')
