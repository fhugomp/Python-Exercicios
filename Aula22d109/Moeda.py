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
