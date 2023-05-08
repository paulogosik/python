saque = int(input('=> Informe o valor do saque: '))
print('=======================')

n100 = saque // 100
n50 = (saque - (n100 * 100)) // 50
n10 = (saque - ((n50 * 50) + (n100 * 100))) // 10
n5 = (saque - ((n10 * 10) + (n50 * 50) + (n100 * 100))) // 5
m1 = (saque - ((n5 * 5) + (n10 * 10) + (n50 * 50) + (n100 * 100))) // 1

print(f'=> Saque: R${saque}\n'
      f'=> Nota de R$100: {n100} - (R${n100 * 100})\n'
      f'=> Nota de R$50: {n50} - (R${n50 * 50})\n'
      f'=> Nota de R$10: {n10} - (R${n10 * 10})\n'
      f'=> Nota de R$5: {n5} - (R${n5 * 5})\n'
      f'=> Moeda de R$1 : {m1} - (R${m1 * 1})\n')
