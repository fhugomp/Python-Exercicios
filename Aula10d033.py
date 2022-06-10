n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite outro número: '))
mv = n1  # Vou determinar o n1 como o menor e escrever 'ifs' se ele não for
if n2 < n1 and n2 < n3:
    mv = n2
if n3 < n1 and n3 < n2:
    mv = n3
print(f'O menor valor entre "{n1, n2, n3}" é: {mv}')
maiv = n1  # Vou determinar o n1 como maior e colocar 2 'ifs'(do n2 e do n3) se não for.
if n2 > n1 and n2 > n3:
    maiv = n2
if n3 > n1 and n3 > n2:
    maiv = n3
print(f'O maior valor entre"{n1, n2, n3}" é: {maiv}')
