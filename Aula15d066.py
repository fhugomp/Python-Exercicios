# SOMA DE NUMEROS INTEIROS
soma = contador = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    soma += n
    contador += 1
print(f'Você digitou {contador} números e a soma entre eles é: {soma}')
