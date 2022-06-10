# FALANDO QUAIS AS VOGAIS DE UMA PALAVRA PRESENTE DENTRO DE UMA TUPLA
pal = ('Vou', 'Ser', 'Programador', 'Meu', 'Futuro', 'Sera', 'Brilhante')
for p in pal:
    print(f'\nA palavra é "{p.upper()}" e nela contém as vogais:', end='')
    for l in p:
        if l.lower() in 'aeiou':
            print(l, end=' ')
