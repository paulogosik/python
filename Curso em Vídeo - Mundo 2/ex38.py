n1 = int(input('=> Type an integer number: '))
n2 = int(input('=> Type another integer number: '))

if n1 > n2:
    print(f'The number {n1} is bigger than the number {n2}!')
elif n2 > n1:
    print(f'The number {n2} is bigger than the number {n1}!')
else:
    print(f'There are no bigger number, {n1} and {n2} are equal numbers!')