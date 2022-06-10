# PERGUNTA NOME E PESO E NO FINAL MOSTRA O MENOR E O MAIOR PESO E O NOME DA PESSOA CORRESPONDENTE
pessoas = list()
dado = list()
contador = mai = men = 0
while True:
    dado.append(str(input('Nome:')))
    dado.append(float(input('Peso:')))

    if len(pessoas) == 0:
        mai = men = dado[1]
    else:
        if dado[1] > mai:
            mai = dado[1]

        if dado[1] < men:
            men = dado[1]

    pessoas.append(dado[:])
    cont = str(input('Quer continuar?[S/N]')).strip().upper()
    contador += 1
    dado.clear()
    while cont not in 'SN':
        cont = str(input('Opção Inválida. Quer continuar?[S/N]')).strip().upper()
    if cont in 'N':
        break

print('=' * 35)
print(f'No total tiveram {contador} pessoas cadastradas.')
print('E entre eles:')
print(f'O maio peso foi: {mai}Kg. Peso de ', end='')

for p in pessoas:
    if p[1] == mai:
        print(f'{p[0]}', end=', ')

print(f'E o menor peso foi: {men}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == men:
        print(f'{p[0]}', end=', ')
