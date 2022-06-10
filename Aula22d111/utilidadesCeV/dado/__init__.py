def leiadinheiro():
    while True:
        n = str(input('Digite um Valor: R$ ')).strip().replace(',', '.')
        if n.isalpha() or n == '':
            print(f'\033[31mERRO! "{n}" não é um número válido\033[m')
        else:
            return float(n)
