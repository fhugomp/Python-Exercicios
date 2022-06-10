# PERGUNTANDO NÚMEROS E OS COLOCANDO EM UMA LISTA EM ORDEM CRESCENTE
lisnum = []
conti = ''
while True:
    n = (int(input('Digite um número: ')))
    if n not in lisnum:
        lisnum.append(n)
        print('Valor adicionado!')
    else:
        print('Valor duplicado! Valor não adicionado')
    conti = str(input('Você quer continuar?[S/N] ')).strip().upper()
    while conti not in 'SN':
        conti = str(input('Você quer continuar?[S/N] ')).strip().upper()
    if conti in 'N':
        break
lisnum.sort()
print(f'Os valores digitados foram: {lisnum}')
