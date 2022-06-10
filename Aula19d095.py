jogadores = []
dados = dict()
lgols = list()
while True:
    dados.clear()
    dados['Nome'] = str(input('Nome do Jogador: '))
    partidas = int(input('Quantas partidas ele jogou? '))
    for c in range(1, partidas + 1):
        lgols.append(int(input(f'Quantos Gols ele fez na partida {c}? ')))
    dados['Gols'] = lgols[:]
    lgols.clear()
    dados['Total de Gols'] = sum(dados['Gols'])
    jogadores.append(dados.copy())
    flag = str(input('Adicionar mais jogadores? [S/N]')).strip().upper()
    while flag not in 'SN':
        flag = str(input('ERRO! Responda apenas com S ou N: ')).strip().upper()
    if flag in 'N':
        break
print('~~' * 22)
print('c.', end='')
for i in dados.keys():
    print(f'{i:<12}', end='')
print()
print('~~' * 22)
for k, v in enumerate(jogadores):
    print(f'{k:3>}', end=' ')
    for j in v.values():
        print(f'{str(j):<13}', end='')
    print('')
print('999 = Encerra o Programa')
print('~~' * 22)
while True:
    jogescolha = int(input('Digite o número escolhido: '))
    if jogescolha == 999:
        break
    if jogescolha > len(jogadores):
        jogescolha = int(input('ERRO! Digite um número válido: '))
    else:
        print(f' →→ TABELA DE GOLS DO(A) {jogadores[jogescolha]["Nome"]}:')
        print(f'   →→ {jogadores[jogescolha]["Nome"]} Jogou ao todo {len(jogadores[jogescolha]["Gols"])} partida(s)')
        for i, g in enumerate(jogadores[jogescolha]['Gols']):
            print(f'      - No jogo {i + 1} fez {g} gols')
print('<< PROGRAMA ENCERRADO >>')
