l1 = float(input('=> Digite um lado adjacente: '))
l2 = float(input('=> Digite outro lado adjacente: '))
print('--------------')

if l1 == l2:
    print('=> O quadrilátero é um quadrado perfeito!')
elif l1 > l2:
    print(f'=> O quadrilátero é um retângulo!\n'
          f'=> Lado maior: {l1}')
else:
    print(f'=> O quadrilátero é um retângulo!\n'
          f'=> Lado maior: {l2}')