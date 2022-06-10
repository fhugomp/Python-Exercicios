def notas(*n, sit=False):
    """
    → Programa que cria um dicionário com n notas, mostrando o total de notas, a maior nota,
      a menor, a média, e se desejado a situação das notas em geral.
    :param n: Notas
    :param sit: (Opcional) mostra a situação das notas
    :return: Retorna o dicionário.
    """
    r = dict()
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    media = (sum(n)) / len(n)
    r['Media'] = media
    if sit:
        if media >= 7:
            r['Situação'] = 'Boa'
        elif 5 < media < 7:
            r['Situação'] = 'Razoavel'
        else:
            r['Situação'] = 'Ruim'
    return r


resp = notas(10, 8, 9, 4, 6, 7, sit=True)
print(resp)
help(notas)