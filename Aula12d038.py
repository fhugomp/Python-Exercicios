val1 = int(input('Digite um número: '))
val2 = int(input('Digite outro valor: '))
if val1 > val2:
    print(f'\033[34mO primeiro valor é maior.')
elif val2 > val1:
    print(f'\033[36mO segundo valor é maior.')
elif val1 == val2:
    print(f'\033[32mOs dois são iguais.')
