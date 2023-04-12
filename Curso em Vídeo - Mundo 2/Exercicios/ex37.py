name = input('=> Hello, what is your name? ')
number = int(input('=> Choose any integer number: '))
print('=> Choose an option between those below:\n'
      ' [1] To convert your number to Binary.\n'
      ' [2] To convert your number to Octal.\n'
      ' [3] To convert your number to Hexadecimal.')
option = int(input('=> What do you chose? '))
print('=========')

if option == 1:
    print(f'=> {name}, your number in Binary is { bin(number) }!')
elif option == 2:
    print(f'=> {name}, your number in Octal is { oct(number) }!')
elif option == 3:
    print(f'=> {name}, your number in Hexadecimal is { hex(number) }!')
else:
    print('=! Invalid option!')