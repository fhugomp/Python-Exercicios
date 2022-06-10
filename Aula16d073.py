times = ('Bragantino', 'Bahia', 'Ceará', 'Fortaleza', 'Athletico-PR', 'Flamengo', 'Atlético-GO', 'Sport Recife',
         'Juventude', 'Cuiabá', 'Internacional', 'São Paulo', 'Fluminense', 'Grêmio', 'Atlético-MG', 'América-MG',
         'Palmeiras', 'Corinthians', 'Chapecoense', 'Santos')
print('\033[36m→' * 91)
print(f'Os Primeiros 5 colocados são: {times[0:5]}')
print('→' * 91)
print(f'Os Últimos 4 colocados são: {times[16:20]}')
print('→' * 91)
print(f'Em ordem alfábetica é: {sorted(times)}')
print('→' * 91)
print(f'E o Fortaleza esta em {times.index("Fortaleza") + 1}ª colocado.')
print('→' * 91)
