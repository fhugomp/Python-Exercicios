c = float(input('Quanto custa a casa?: '))
sal = float(input('Quanto é o seu salário?: R$'))
a = int(input('Em quantos anos para a compra da casa?: '))
ac = a * 12
parcela = c / ac
salpor = sal * 0.30
if parcela >= salpor:
    print(f'\033[33mA parcela mensal equivale a: {parcela:.2f} que é 30% ou mais do seu salário. Então:')
    print(f'Empréstimo \033[31mNegado\033[m.')
else:
    print(f'\n\n\033[32mParebéns a parcela mensal equivale a: {parcela:.2f} que é menos de 30% do seu salário. Então:')
    print('Empréstimo \033[34mAprovado!')
