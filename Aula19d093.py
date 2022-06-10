dados = dict()
lgols = list()
dados['Nome'] = str(input('Nome do Jogador: '))
partidas = int(input('Quantas partidas ele jogou? '))
for c in range(1, partidas + 1):
    lgols.append(int(input(f'Quantos Gols ele fez na partida {c}? ')))
dados['Gols'] = lgols[:]
dados['Total de Gols'] = sum(dados['Gols'])

print('~' * 21, '1º FORMA', '~' * 21)
print(dados)
print('~~' * 26)

print('~' * 21, '2º FORMA', '~' * 21)
for k, v in dados.items():
    print(f'{k}: {v}')
print('~~' * 26)

print('~' * 21, '3º FORMA', '~' * 21)
print(f'O jogador {dados["Nome"]} jogou {partidas} partidas')
for i, v in enumerate(dados['Gols']):
    print(f'  Na {i + 1}º partida, fez {v} gols')
print('~~' * 26)
