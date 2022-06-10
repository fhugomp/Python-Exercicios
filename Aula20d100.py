from random import randint


def sorteio(lista):
    print(f'Os números sorteados foram: ', end='')
    for c in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='')
    print(f'Fim')


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'A soma dos números pares é: {soma}')


numeros = []
sorteio(numeros)
somaPar(numeros)
