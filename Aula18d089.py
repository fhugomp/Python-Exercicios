tudo = list()
con = ''

while con in 'S':
    n = str(input('Nome:')).strip()
    nt1 = float(input('1º Nota: '))
    nt2 = float(input('2º Nota: '))
    media = (nt1 + nt2) / 2
    tudo.append([n, [nt1, nt2], media])
    con = str(input('Continuar adicionando? [S/N]')).strip().upper()

    while con not in 'SN':
        con = str(input('Continuar adicionando? [S/N]')).strip().upper()
    print('=' * 29)
print(f'{"Nº":<4}  {"Nome":<8}  {"Notas":<10}')

for i, n in enumerate(tudo):
    print(f'{i:<4}  {n[0]:<8}  {n[1][0]:>2} / {n[1][1]:>2}')

while True:
    print('=' * 65)
    print('[999 Interrompe a operação]')
    esc = int(input('Você quer ver a média de qual aluno? '))
    if esc == 999:
        print('=' * 29)
        print('Operação Interrompida.')
        break
    if esc <= len(tudo) - 1:
        print(f'O aluno(a) {tudo[esc][0]} tirou as notas: {tudo[esc][1]}'
              f' Portanto sua média é: {tudo[esc][2]}')
