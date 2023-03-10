custo = float(input('=> Qual o custo de fábrica do carro? '))
print('------------------')

distribuidor = custo * 0.28
impostos = custo * 0.45
custof = custo + distribuidor + impostos

print(f'=> Custo final: R${custof:.2f}\n'
      f'=> Impostos: R${impostos:.2f}\n'
      f'=> Porcentagem do distribuidor: R${distribuidor:.2f}')