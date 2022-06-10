ano_nascimento = int(input('Ano de nascimento: '))


def voto(ano):
    from datetime import datetime
    v = datetime.now().year - ano_nascimento
    if 18 <= v < 65:
        return f'Você tem: {v} anos o VOTO É OBRIGATÓRIO'
    if 16 <= v < 18 or v > 65:
        return f'Você tem: {v} anos o VOTO É OPCIONAL'
    if v < 16:
        return f'Você tem: {v} anos: Você NÃO VOTA'


print(voto(ano_nascimento))
