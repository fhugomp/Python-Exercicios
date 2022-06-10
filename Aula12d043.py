altura = float(input('Digite a sua altura: '))
peso = float(input('Digite o seu peso: '))
imc = peso / (altura * altura)
if imc <= 18.5:
    print(f'Seu IMC é: {imc:.1f}, você está \033[33mabaixo do peso ideal\033[m.')
elif 18.5 <= imc <= 25:
    print(f'Seu IMC é: {imc:.1f}, você está no \033[32mpeso ideal\033[m.')
elif 26 <= imc <= 30:
    print(f'Seu IMC é: {imc:.1f}, você está com \033[37msobrepeso\033[m.')
elif 31 <= imc <= 40:
    print(f'Seu IMC é: {imc:.1f}, você está com \033[33mobesidade\033[m.')
else:
    print(f'Seu IMC é: {imc:.1f}, você está com \033[31mobesidade mórbida.')
