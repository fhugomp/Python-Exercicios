dis = int(input('Qual a distância levada em km?: '))
if dis <= 200:
    print(f'A passagem custara: {dis * 0.50}')
else:
    print(f'Sua pasagem vai custar: {dis * 0.45}')
