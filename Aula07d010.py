#Quantos dolaraes eu posso comprar?
r = float(input('\033[32mQuanto você tem?:R$ \033[m'))
d = float(r / 5.27)
e = float(r / 6.40)
i = float(r / 0.048)
#Cotação de 15/05/21
print(f'Com essa quantia você podera comprar:\n\033[33mU${d:.2f}\nEU${e:.2f}\nYEN${i:.2f}')
