from random import shuffle
a1 = input('Nome do aluno: ')
a2 = input('Nome do aluno: ')
a3 = input('Nome do aluno: ')
a4 = input('Nome do aluno: ')
lis = [a1, a2, a3, a4]
shuffle(lis)
print(f'A sequência será: ')
print(lis)
