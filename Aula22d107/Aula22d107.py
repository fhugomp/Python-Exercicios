from Moeda import *
preço = float(input('Digite o preço: R$ '))
print(f'O dobro de R${preço} é R${dobro(preço)}')
print(f'A metade de R${preço} é R${metade(preço)}')
print(f'Com um aumento de 13% fica R${aumentar(preço)}')
print(f'Com um desconto de 10% fica R${diminuir(preço)}')
