p = str(input('Digite uma frase: ')).strip().lower()
ps = p.split()
ju = ''.join(ps)
pi = ''
for l in range(len(ju) - 1, -1, -1):
    pi += ju[l]
if pi == ju:
    print(f'Essa \033[34mé\033[m uma frase pallíndromo.')
else:
    print(f'Essa \033[31mnão é\033[m uma frase palíndromo.')
