n1 = float(input('=> Informe um número: '))
n2 = float(input('=> Informe outro número: '))
print('-----------------------')

media = (n1 + n2) / 2
print(f'=> A média entre os números é igual a: {media}.')

if n1 != n2:
    if n1 < n2:
        quad = n1**2 
        dobro = n2 * 2
        print(f'=> O quadrado do número menor é: {quad}.\n'
              f'=> O dobro do número maior é: {dobro}.')
    else:
        quad = n2**2 
        dobro = n1 * 2
        print(f'=> O quadrado do número menor é: {quad}.\n'
              f'=> O dobro do número maior é: {dobro}.')
else: 
    print('=> Números informados são iguais.')