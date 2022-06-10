preço = float(input('Digite o preço do produto: '))
print('---Métodos de Pagamento---')
print('[1] Dinheiro/Cheque')
print('[2] Cartão de Débito')
print('[3] Cartão de Crédito(Até 2x)')
print('[4] Cartão de Crédito(3x ou mais)')
pagamento = str(input('Digite um dos número acima para escolher o método de pagamento:\n')).strip()

if pagamento == '1' or pagamento == '2' or pagamento == '3' or pagamento == '4':
    if pagamento == '1':
        print(f'O preço com um desconto de 10% será: \033[32m{(90 * preço) / 100}\033[m.')
    elif pagamento == '2':
        print(f'O preço com um desconto de 5% será: \033[32m{(95 * preço) / 100}\033[m.')
    elif pagamento == '3':
        print(f'O preço será: \033[32m{preço}\033[m.')
    elif pagamento == '4':
        print(f'O preço com 20% de juros será: \033[32m{(120 * preço) / 100}\033[m.')
    print('\033[36mObrigado pela preferência tenha um Bom Dia!')
else:
    print('Opção Inválida.')
