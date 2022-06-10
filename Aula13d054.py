from datetime import date
atual = date.today().year
maior = 0
menor = 0
pessoas = 0
for nas in range(1, 8):
    anascimento = int(input(f'Digite o ano de nascimento da {nas}º pessoa: '))
    idade = atual - anascimento
    pessoas += 1
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print(f'\n\033[36mO total de pessoas foi {pessoas} e entre elas tem:\n{maior} pessoa(s) \033[34mmaiores de idade\033[m '
      f'\033[36me {menor} pessoa(s) \033[33mmenores de idade\033[m\033[36m.')
