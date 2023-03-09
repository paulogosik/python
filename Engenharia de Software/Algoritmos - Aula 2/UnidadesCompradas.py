un1 = int(input('=> Unidades compradas do produto 1: '))
preco1 = float(input('=> Valor das unidades do produto 1: '))
un2 = int(input('=> Unidades compradas do produto 2: '))
preco2 = float(input('=> Valor das unidades do produto 2: '))
print('----------------------------')

total1 = un1 * preco1
total2 = un2 * preco2

print(f'=> Valor a ser pago do produto 1: R${total1:.2f}\n'
      f'=> Valor a ser pago do produto 2: R${total2:.2f}')