from datetime import date
a = int(input('Qual ano vai ser analisado? Digite 0 se quiser o ano atual: '))
if a == 0:
    a = date.today().year  # Analisa o ano atual
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:  # Formula para calcular o ano biissexto
    print(f'O ano {a} é um ano Bissexto!')
else:
    print(f'O ano {a} não é Bissexto!')
