value = float(input('=> What is the price of the product? '))
print(f'=> What is the payment method? Choose an option below to continue.\n'
      f'    [1] In cash\n'
      f'    [2] In cash on the check\n'
      f'    [3] By card\n'
      f'    [4] Up to 2x by card\n'
      f'    [5] 3x or more by card')
option = int(input('=> '))
print('---------')

if option == 1 or option == 2:
    discount = value * 0.1
    price = value - discount
    print(f'=> Original price: ${value:.2f}\n'
          f'=> Discount: ${discount:.2f}\n'
          f'=> Actual price: ${price:.2f}')
elif option == 3:
    discount = value * 0.05
    price = value - discount
    print(f'=> Original price: ${value:.2f}\n'
          f'=> Discount: ${discount:.2f}\n'
          f'=> Actual price: ${price:.2f}')
elif option == 4:
    print(f'=> Original price: ${value}\n'
          f'=> Actual price: ${value}')
elif option == 5:
    interest = value * 0.2
    price = value + interest
    print(f'=> Original price: ${value}\n'
          f'=> Interest rate: ${interest}\n'
          f'=> Actual price: ${price}')
else:
    print('=> INVALID OPTION')