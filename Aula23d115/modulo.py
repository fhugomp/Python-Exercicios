from time import sleep


def menu():
    while True:
        cabeçalho('SISTEMA DE CADASTRAMENTO')
        print('1 - Cadastrar uma nova pessoa'
              '\n2 - Ver as pessoas cadastradas'
              '\n3 - Encerrar programa')
        print('=' * 35)
        try:
            flag = int(input('Qual das opções? '))
        except ValueError:
            print('\033[1:31mERRO! Digite um número válido.\033[m')
            continue
        if flag > 3 or flag < 1:
            print('\033[1:31mERRO! Escolha uma opção existente.\033[m')
        if flag == 1:
            cabeçalho('NOVO CADASTRO')
            cadastrar()
        if flag == 2:
            cabeçalho('PESSOAS CADASTRADAS')
            ler_arquivo()
            sleep(3.5)
        if flag == 3:
            print('Encerrando o Programa...')
            sleep(1.5)
            break


def cadastrar():
    with open('Cadastro De Pessoas.txt', 'a') as arquivo:
        nome = str(input('Nome: '))
        idade = str(input('Idade: '))
        arquivo.write(f'{nome}')
        arquivo.write(f'\t\t{idade} anos')
        print(f'{nome} cadastrado(a) com sucesso.')
        sleep(1.5)


def ler_arquivo():
    with open('Cadastro De Pessoas.txt', 'r') as arquivo:
        mensagem = arquivo.read()
        print(mensagem)


def arquivo_existe(nome):
    try:
        a = open(nome, 'r')
        a.close()
    except FileNotFoundError:
        criar_arquivo(nome)
        print('Arquivo criado com sucesso')
    else:
        print('Arquivo Existente')


def criar_arquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('ERRO!')
    else:
        print(f'{nome} criado com sucesso')


def cabeçalho(txt):
    print('=' * 35)
    print(f'{txt:^35}')
    print('=' * 35)
