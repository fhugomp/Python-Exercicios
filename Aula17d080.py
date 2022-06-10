# PERGUNTANDO 5 NÚMEROS E OS COLOCANDO EM ORDEM CRESCENTE SEM O SORTED
n = []
for c in range(0, 5):
    nad = int(input('Digite um número: '))
    if c == 0 or nad > n[-1]:
        n.append(nad)
        print('Número adicionado no final da lista')
    else:
        pos = 0
        while pos < len(n):
            if nad <= n[pos]:
                n.insert(pos, nad)
                print(f'Adicionado na posição {pos} da lista')
                break
            pos += 1
print(f'Os números digitados em ordem são: {n}')
