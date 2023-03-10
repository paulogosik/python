n1 = int(input('=> Digite um número inteiro: '))
n2 = int(input('=> Digite outro número inteiro: '))
print('----------------')

soma = n1 + n2
resto = soma % 2

if resto == 0:
    soma = soma / 2
    print(f'=> NÚMERO PAR!\n'
          f'=> A metade da soma é: {soma}')
else:
    print('=> NÚMERO ÍMPAR!')