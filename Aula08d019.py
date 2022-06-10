from random import choice
a1 = input('Digite o nome do aluno: ')
a2 = input('Digite o nome de outro aluno: ')
a3 = input('Digite o nome de outro aluno: ')
a4 = input('Digite o nome de outro aluno: ')
lis = [a1, a2, a3, a4]
es = random.choice(lis)
print(f'O aluno(a) selecionado é: {es}')
