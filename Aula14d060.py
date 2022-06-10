from math import factorial
f = 'S'
while f == 'S':
    n = int(input('Digite um número: '))
    print(f'O fatorial será: {factorial(n)}')
    f = str(input('Quer tentar novamente?[S/N] ')).strip().upper()
print('Operação Finalizada.')
