c = 0
a = int(input('=> Type me a random number: '))
b = int(input('=> Type another random number: '))
print('====================')

c = a
a = b
b = c

print(f'=> First changed number: {a}\n'
      f'=> Second changed number: {b}')