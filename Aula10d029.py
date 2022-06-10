vel = int(input('Qual a velocidade do carro?: '))
mul = (vel - 80) * 7
if vel > 80:
    print(f'Você esta acima do limite permitido de 80km/h')
    print(f'Você foi multado em R${mul}')
else:
    print('Parabéns você esta dentro do limite permitido.')
    print('Continue dirigindo em segurança.')
