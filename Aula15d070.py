# Loja
print('=' * 25)
print(f'{"Seja Bem-Vindo(a)":^25}')
print('=' * 25)
print(f'{"O QUE VAI COMPRAR?":^25}')
print('_' * 25)
total = maisqmil = preçobarato = contad = 0
pmbarato = ''
while True:
    nome = str(input('Digite o nome do produto:\n'))
    preço = float(input('Digite o preço:\nR$'))
    conti = str(input('Continuar comprando?[S/N]:\n')).strip().upper()
    total += preço
    contad += 1
    while conti not in 'SN':
        conti = str(input('Continuar comprando?[S/N]: ')).strip().upper()
    if contad == 1:
        preçobarato = preço
        pmbarato = nome
    else:
        if preço < preçobarato:
            preçobarato = preço
            pmbarato = nome
    if preço >= 1000:
        maisqmil += 1
    if conti == 'N':
        break
print('A sua compra:')
print(f'Custou um total de: R${total}')
print(f'Teve {maisqmil} produto(s) que custaram mais de R$1000.00')
print(f'E o produto mais barato foi: {pmbarato} e ele custa: {preçobarato}')
