num_fatorial = int(input('Digite um número: '))
while True:
    mostrar_conta = int(input('Digite 0: Mostra a conta\n'
                              'Digite 1: Não mostra a conta\n'))
    print('~~' * 26)
    if mostrar_conta != 1 and mostrar_conta != 0:
        print('ERRO! Digite apenas 1 ou 0')
    else:
        break
if mostrar_conta == 0:
    show = True
else:
    show = False


def fatorial(n, show=False):
    """
    → Programa para fatorar um número podendo ver ou não a sua conta.
    :param n: Número que será fatorado
    :param show: Parâmetro para mostrar ou não a conta da fatoração
    :return: retorna o resultado da fatoração
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print(fatorial(num_fatorial, show))
