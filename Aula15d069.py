# CADATRAMENTO DE PESSOAS
pessoas18 = mulheres20 = thomens = 0
while True:
    print('=' * 24)
    print('Cadastramento De Pessoas')
    print('=' * 24)
    idade = int(input('Digite a Idade: '))
    sexo = str(input('Qual o Sexo?[M/F]: ')).strip().upper()
    while sexo not in 'MF':
        sexo = str(input('Qual o Sexo?[M/F]: ')).strip().upper()
    con = str(input('Você quer continuar?[S/N]: ')).strip().upper()
    while con not in 'SN':
        con = str(input('Você quer continuar?[S/N]: ')).strip().upper()
    if idade >= 18:
        pessoas18 += 1
    if sexo == 'M':
        thomens += 1
    if sexo == 'F' and idade < 20:
        mulheres20 += 1
    if con == 'N':
        break
print(f'\nDas pessoas cadastradas tiveram:\n{pessoas18} pessoa(s) adulta(s) cadastrada(s)')
print(f'{thomens} pessoa(s) do sexo Masculino cadastrada(s)')
print(f'{mulheres20} pessoa(s) do sexo Feminino com menos de 20 anos cadastrada(s)')
