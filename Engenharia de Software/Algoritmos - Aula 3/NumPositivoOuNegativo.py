num = float(input('=> Digite qualquer número: '))

if num > 0:
    print('=> O número é positivo!')
    num = num * 2
    print(f'=> O dobro do seu número é: {num}!')
elif num < 0:
    print('=> O número é negativo!')
    if num % 2 == 0:
        print('=> O número é par!')
    else:
        print('=> O número é ímpar!')
else:
    print('=> O valor é igual a zero!')