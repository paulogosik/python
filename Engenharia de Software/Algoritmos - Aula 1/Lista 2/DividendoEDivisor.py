print('=> Type two numbers integers and different from zero.')
dividend = int(input('=? First number: '))
divider = int(input('=? Second number: '))
print('=========')

quotient = dividend // divider
rest = dividend % divider

print(f'=> Dividend: {dividend}\n'
      f'=> Divider: {divider}\n'
      f'=> Quotient: {quotient}\n'
      f'=> Rest: {rest}')