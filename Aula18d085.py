todos = []
pares = []
impares = []

for n in range(0, 7):
    num = int(input('Digite um número: '))

    if num % 2 == 0:
        pares.append(num)
        pares.sort()

    else:
        impares.append(num)
        impares.sort()

todos.append(pares)
todos.append(impares)

print('=' * 45)
print(f'Os números pares digitados foram: {todos[0]}')
print(f'E os números impares foram: {todos[1]}')
