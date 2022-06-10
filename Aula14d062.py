ptermo = int(input('Digite o Primeiro termo da PA: '))
razao = int(input('Digite a Razão: '))
cont = 1
termo = ptermo
maist = 10
totalt = 0
while maist != 0:
    totalt += maist
    while cont <= totalt:
        termo += razao
        cont += 1
        print(f'{termo} ; ', end='')
    print(f'Pausa')
    maist = int(input('Digite quantos termos à mais: '))
print(f'Fim da PA. Com um total de {cont} termos.')
