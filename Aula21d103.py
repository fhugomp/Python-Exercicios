nome_jogador = str(input('Nome do Jogador(a): ')).strip()
gols = str(input('Gols feitos: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0


def ficha(nome='', g=0):
    """
    →Programa que pergunta o nome e quantos gols um jogador fez
    podendo ambos os campos serem respondidos com nada
    :param nome: Nome do jogador(a)
    :param g: Gols feitos
    :return: Retorna uma frase formatado com o nome e a quantidade de gols feitos.
    """
    if nome == '':
        nome = '<desconhecido>'
    if g == '':
        g = 0
    return f'O jogador(a) {nome} fez {g} gol(s) no campeonato.'


print(ficha(nome_jogador, gols))
