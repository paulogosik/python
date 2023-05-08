n1 = float(input('=> Digite um número: '))
n2 = float(input('=> Digite outro número: '))
print('----------------')

if n2 == 0:
    print('=> Não pode ser feita divisão por zero!')
else: 
    div = n1 / n2
    print(f'=> O resultado da divisão é: {div}')