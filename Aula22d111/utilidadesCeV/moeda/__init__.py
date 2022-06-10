def aumentar(num, aum=13):
    n = num + (num * aum / 100)
    return n


def diminuir(num, des=10):
    n = num - (num * des / 100)
    return n


def dobro(num):
    n = num * 2
    return n


def metade(num):
    n = num / 2
    return n


def moeda(num, f=True):
    if f:
        n = num
        return f'R${n:.2f} '.replace('.', ',')
    else:
        return num


def resumo(num, aum=13, des=10):
    print('=' * 35)
    print(f'{"RESUMO DO VALOR":^35}')
    print('=' * 35)
    print(f'Valor Digitado: \t{moeda(num)}')
    print(f'Metade do Valor: \t{moeda(metade(num))}')
    print(f'O Dobro: \t\t\t{moeda(dobro(num))}')
    print(f'Aumentado {aum}%: \t\t{moeda(aumentar(num, aum))}')
    print(f'Diminuindo {des}%:   \t{moeda(diminuir(num, des))}')
    print('=' * 35)
