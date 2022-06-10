c = ('\033[m',  # 0 - Sem cor
     '\033[1:30:41m'  # 1 - Vermelho
     '\033[1:30:42m'  # 2 - Verde
     '\033[1:30:43m'  # 3 - Amarelo
     '\033[1:30:46m'  # 4 - Ciano
     '\033[1:30:107m')  # 5 - Branco


def ajuda(com):
    help(com)


def titulo(txt, cor=0):
    tam = len(txt) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {txt}')
    print('~' * tam)
    print(c[0], end='')


comando = ''
while True:
    titulo('AJUDAS PyHelp', 1)
    comando = str(input('Função ou Lib: '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('< VOLTE SEMPRE >', 1)
