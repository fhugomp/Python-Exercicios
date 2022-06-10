from math import hypot
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimeto do cateto adjacente: '))
hp = hypot(co , ca)
print(f'O resultado é: {hp:.2f}')
'''A formula para resolver sem a importação é (co ** 2 + ca ** 2) **(1/2)'''
