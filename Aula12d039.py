from datetime import date
ano_nascimento = int(input('\033[34mAno de nascimento: '))
print('Digite o número correspondente ao sexo a seguir:')
print('[0] Masculino')
print('[1] Feminino')
sexo = str(input('Digite uma das opções acima: ')).strip()
ano_atual = date.today().year
idade = ano_atual - ano_nascimento
if sexo == '0':
    print(f'\033[97Quem nasceu em {ano_nascimento} tem {idade} anos em {ano_atual}.\033[m')
    if idade > 18:
        print(f'\033[31mVocê já deveria ter se alistado há {idade - 18} ano(s), no ano de {ano_nascimento + 18}')
    elif idade == 18:
        print('\033[32mJá está no ano de você se alistar.')
    else:
        print(f'\033[36mAinda faltam {18 - idade} ano(s) para você se alistar, no ano de {ano_nascimento + 18}')
elif sexo == '1':
    print('O alistamento não é necessario para pessoas do sexo feminino.')
else:
    print('Opção inválida. Tente novamente.')
