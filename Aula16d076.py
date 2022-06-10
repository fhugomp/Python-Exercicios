# LISTA DE COMPRAS TABULADA
lista = ('Monitor', 1350.00, 'Teclado', 225.00, 'Mouse', 179.00,
         'Mouse Pad', 73.50, 'Controle', 150.00, 'Computador', 7539.50)
print('~' * 35)
print(f'{"Lista De Compras":^35}')
print('~' * 35)
for l in range(0, len(lista)):
    if l % 2 == 0:
        print(f'{lista[l]:.<26}', end='')
    else:
        print(f'R$ {lista[l]:>}')
print('~' * 35)
