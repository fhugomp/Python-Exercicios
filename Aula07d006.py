n = int(input('\033[97mDigite um número:\033[m '))
m1 = n * 2
m2 = n * 3
rq = n ** (1/2)  # Essa é a formula pra calcular a raiz quadrada(Subistituir o 2 pra mudar a raiz)
print(f'O seu dobre é: \033[31m{m1}\033[m \nO seu triplo é: \033[36m{m2}\033[m \nE a sua raiz quadrada é: \033[33m{rq:.2f}\033[m.')

