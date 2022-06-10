soma = 0
cont = 0
n = 0
while n != 999:
    n = int(input('Digite um número[999 = Stop]: '))
    if n != 999:
        soma += n
        cont += 1
print(f'Você digitou: {cont} número(s) e a soma deles é: {soma}.')
