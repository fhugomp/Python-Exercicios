lar = float(input('Quantos metros a parede tem de largura?: '))
alt = float(input('Quantos metros a parede tem de altura?: '))
are = float(lar * alt)
tin = float(are / 2)
#lar==Largura, alt==Altura, are==Área, tin==Tinta
print(f'A sua área é de: {are}m², você precisara de {tin}l de tinta para pinta-la.')
