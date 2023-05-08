sexo = input('=> Digite "H" para homem ou "M" para mulher: ')
sexo = sexo.upper()
altura = float(input('=> Qual a altura em M? '))
peso = float(input('=> Qual o peso em quilogramas? '))
print('---------------------')

imc = peso / (altura**2)

if sexo == 'M':
    if imc > 20.8:
        print(f'=> Acima do peso ideal. IMC: {imc:.2f}')
    elif imc == 20.8:
        print(f'=> Peso ideal. IMC: {imc:.2f}')
    else:
        print(f'=> Abaixo do peso ideal. IMC: {imc:.2f}')
elif sexo == 'H':
    if imc > 22:
        print(f'=> Acima do peso ideal. IMC: {imc:.2f}')
    elif imc == 22:
        print(f'=> Peso ideal. IMC: {imc:.2f}')
    else:
        print(f'=> Abaixo do peso ideal. IMC: {imc:.2f}')
else:
    print('=> Opção "SEXO" indisponível.')
    