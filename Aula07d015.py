km = float(input('Quantos Km foram rodados?: '))
dia = int(input('Quantos dias ele foi alugado?: '))
pre = dia * 60 + (km * 0.15)
print(f'O valor que você deve pagar é: R${pre:.2f}.')
