from datetime import datetime
dados = dict()
dados['Nome'] = str(input('Nome: ')).strip()
ano = int(input('Ano de Nascimento: '))
dados['Idade'] = datetime.now().year - ano
dados['CTPS'] = int(input('Carteira de Trabalho[0 = Não tem]: '))
if dados['CTPS'] == 0:
    print('~~' * 20)
    for k, v in dados.items():
        print(f'  - {k}: {v}')
else:
    dados['Contratação'] = int(input('Ano de Contratação: '))
    dados['Sálario'] = float(input('Sálario: R$ '))
    dados['Aposentadoria'] = dados['Idade'] + ((dados['Contratação'] + 35) - datetime.now().year)
    print('~~' * 20)
    for k, v in dados.items():
        print(f'  - {k}: {v}')
