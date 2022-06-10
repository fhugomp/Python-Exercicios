todos = []
mulheres = []
pessoas = {}
soma = media = 0

while True:
    pessoas.clear()
    pessoas['Nome'] = str(input('Nome: ')).strip()
    pessoas['Sexo'] = str(input('Sexo: [M/F] ')).strip().upper()

    while pessoas['Sexo'] not in 'MF':
        pessoas['Sexo'] = str(input('Erro! Responda apenas com M ou F: ')).strip().upper()
    pessoas['Idade'] = int(input('Idade: '))
    soma += pessoas['Idade']
    if pessoas['Sexo'] == 'F':
        mulheres.append(pessoas.copy())
    todos.append(pessoas.copy())
    flag = str(input('Quer Continuar? [S/N] ')).strip().upper()

    while flag not in 'SN':
        flag = str(input('Erro! Responda apenas com S ou N: ')).strip().upper()

    if flag == 'N':
        break
media = soma / len(todos)
print('~~' * 28)
print(f'Ao todo foram cadatradas: {len(todos)} pessoas.')
print(f'A média das pessoas cadastradas é: {media}')
print(f'As mulheres cadastradas foram:', end=' ')
for n in mulheres:
    print(f'{n["Nome"]}', end='; ')
print('\nAs pessoas com idade acima da média são: ')
for i in todos:
    if i['Idade'] > media:
        for k, v in i.items():
            print(f'{k}: {v}', end=' ')
