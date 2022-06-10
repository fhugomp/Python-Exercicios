# LENDO VÁRIOS NÚMEROS E OS COLOCANDO EM UMA LISTA E NO FINAL OS SEPARANDO EM LISTAS DE PARES E IMPARES
lista = []
listaim = []
listapa = []
while True:
    lista.append(int(input('Digite um número: ')))
    r = str(input('Você quer continuar?[S/N]')).strip().upper()
    while r not in 'SN':
        r = str(input('Tente Novamente. Deseja continuar?[S/N] ')).strip().upper()
    if r in 'N':
        break
for v in lista:
    if v % 2 == 0:
        listapa.append(v)
    else:
        listaim.append(v)
print(f'Você digitou os números: {lista}')
print(f'Entre eles os Pares são: {listapa}')
print(f'E os Impares são: {listaim}')
