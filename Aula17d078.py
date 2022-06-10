# LENDO 5 NÚMEROS INTEIROS E FALANDO QUAL O MAIOR, QUAL O MENOR E SUAS RESPECTIVAS POSIÇÕES
num = list()
men = mai = 0
for n in range(0, 5):
    num.append(int(input('Digite um número: ')))
    if n == 0:
        men = mai = num[n]
    else:
        if num[n] > mai:
            mai = num[n]
        if num[n] < men:
            men = num[n]
print(f'Os números presentes na lista são:{num} ', end='')
print(f'\nO maior número foi {mai} e ele está na posição: ', end='')
for p, v in enumerate(num):
    if v == mai:
        print(f'{p}, ', end='')
print()
print(f'E o menor número digitado foi: {men} e ele está na posição:', end='')
for p, v in enumerate(num):
    if v == men:
        print(f'{p}, ', end='')
