from Moeda import *
preço = float(input('Digite o preço: R$ '))
print(f'O dobro de {moeda(preço)} é {moeda(dobro(preço))}')
print(f'A metade de {moeda(preço)} é {moeda(metade(preço))}')
print(f'Com um aumento de 13% fica {moeda(aumentar(preço))}')
print(f'Com um desconto de 10% fica {moeda(diminuir(preço))}')
