sal = float(input('Quanto é o seu salário?: '))
if sal > 1250:
    print(f'O seu salário com um aumento de 10% vai ser: {sal * 0.10 + sal}')
else:
    print(f'O seu novo salário com um aumento de 15% vai ser: {sal * 0.15 + sal}')
