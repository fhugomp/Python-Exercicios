somadi = 0
media = 0
midade = 0
nvelho = ''
mulheresc20 = 0
for p in range(1, 5):
    print(f'==== {p}º Pessoa')
    nome = str(input(f'Digite o nome da pessoa: '))
    idade = int(input(f'Digite a idade da pessoa: '))
    sexo = str(input('Qual o sexo da pessoa? [M/F] ')).strip()
    somadi += idade
    if idade == 1 and sexo in 'Mm':
        midade = idade
        nvelho = nome
    if sexo in 'Mm' and idade > midade:
        midade = idade
        nvelho = nome
    if sexo in 'Ff' and idade < 20:
        mulheresc20 += 1
mediaidade = somadi / 4
print(f'A média de idade é: {mediaidade} ano(s)')
print(f'O homem mais velho tem {midade} ano(s) e tem o nome de {nvelho}.')
print(f'E tem um total de {mulheresc20} mulheres com menos de 20 anos.')
