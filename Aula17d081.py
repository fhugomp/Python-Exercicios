# LENDO VÁRIOS NÚMEROS E NO FINAL DIZENDO QUANTOS NÚMEROS SÃO, QUAL SUA ORDEM DECRESCENTE E SE O 5 ESTÁ NA LISTA
ln = []
while True:
    ln.append(input('Digite um número: '))
    r = str(input('Você deseja continuar?[S/N] ')).strip().upper()
    while r not in 'SN':
        r = str(input('Tente Novamente. Deseja continuar?[S/N] ')).strip().upper()
    if r in 'N':
        break
ln.sort(reverse=True)
print(f'Você digitou: {len(ln)} números')
print(f'Esses números em ordem decrescente fica: {ln}')
if '5' in ln:
    print('O número 5 está presente na lista')
else:
    print('O número 5 não está presente na lista')
