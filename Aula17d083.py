# DIZENDO SE A ESPRESSÃO ESTA CORRETA BASEANDO-SE NA QUANTIDADE DE PARENTESES
ex = str(input('Digite a expressão: '))
paren = []
for par in ex:
    if par == '(':
        paren.append('(')
    elif par == ')':
        if len(paren) > 0:
            paren.pop()
        else:
            paren.append(')')
            break
if len(paren) == 0:
    print('Sua expressão está correta')
else:
    print('Sua expressão está incorreta')
