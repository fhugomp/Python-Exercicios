n1 = float(input('\033[36mDigite a primeira nota: '))
n2 = float(input('\033[36mDigite a segunda nota: '))
m = (n1 + n2) / 2
if m < 5.0:
    print(f'\n\033[36mSua média foi: {m:.1f}. \033[31mReprovado!')
elif 7 > m >= 5:
    print(f'\n\033[36mSua média foi: {m:.1f}. Você está de \033[33mRecuperação.')
elif m >= 7.0:
    print(f'\n\033[36mSua média foi: {m:.1f}. \033[34mAprovado! \033[32mParabéns.')
