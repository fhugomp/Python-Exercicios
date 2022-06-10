# LENDO UM NÚMERO INTEIRO E ESCRVENDO ELE POR EXTENSO
extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
           'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        print(f'O Número digitado foi: \033[36m{extenso[num]}\033[m\n')
        cond = str(input('Você quer Continuar? [S/N]')).strip()
        if cond in 'Nn':
            break
