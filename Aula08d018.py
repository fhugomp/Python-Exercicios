from math import sin, cos, tan, radians
ang = float(input('Digite o ângulo que você quer calcular: '))
s = sin(radians(ang))
print(f'O ângulo {ang} tem o Seno de: {s:.2f}')
co = cos(radians(ang))
print(f'O ângulo {ang} tem o cosseno de: {co:.2f}')
ta = tan(radians(ang))
print(f'O ângulo {ang} tem a Tangente de:{ta:.2f}')
