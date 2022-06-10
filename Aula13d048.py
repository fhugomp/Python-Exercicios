s = 0
con = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        con = con + 1
        s = s + c
print(f'A soma dos {con} números é: {s}.')
