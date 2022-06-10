matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = []
tercoluna = []
seglinhamax = []

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um número para [{l}, {c}] da matriz: '))
        if matriz[l][c] % 2 == 0:
            pares.append(matriz[l][c])
        if c == 2:
            tercoluna.append(matriz[l][c])
        if l == 1:
            seglinhamax.append(matriz[l][c])

print('~~' * 25)

for l in range(0, 3):
    for c in range(0, 3):
        print(f'|{matriz[l][c]:^5}|', end='')
    print()

print('~~' * 25)
print(f'A soma de todos os valores pares é: {sum(pares)}')
print(f'A soma de todos os valores da 3ª coluna é: {sum(tercoluna)}')
print(f'E o maior número da segunda linha é: {max(seglinhamax)}')
