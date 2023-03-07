name = input('=> What is your full name? ')
email = input('=> What is your e-mail? ')

print('------------------')
print(f'Congratulations, {name}! Your account was registered succesfully and you won a 10% discount coupon in your first shop!')
print('------------------')

value = float(input('=> Type the full value of your shop: '))
print('------------------')

discount = value * 0.1
tValue = value - discount

print(f'Total value of the shopping: ${value}\n'
      f'The discount was: ${discount}\n'
      f'The final value is: ${tValue}')