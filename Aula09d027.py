nome = str(input('Digite seu nome completo: ')).strip()
pnome = nome.split()
print(f'Olá, {pnome[0]} seja bem-vindo(a)')
print(f'Seu primeiro nome é {pnome[0]} e o seu ultimo nome é {pnome[len(pnome) - 1]} não é mesmo?')
