p = (input('Digite algo: '))
print(f'É um \033[36mnúmero?\033[m {p.isnumeric()}')
print(f'Esta em \033[31mmaisculo?\033[m {p.isupper()}')
print(f'Esta em \033[34mminusculo?\033[m {p.islower()}')
