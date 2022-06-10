per = 'S' or 'N'
cont = soma = maior = menor = 0
while per == 'S':
    n = float(input('Digite um número: '))
    per = str(input('Você quer continuar? [S/N]')).strip().upper()
    cont += 1
    soma += n
    media = soma / cont
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
print(f'Você digitou {cont} número(s). A média entre eles é: {media:.1f}.')
print(f'E o maior número é: {maior:.0f} e o menor: {menor}')
