print('=> Type 3 integers and positive numbers.')
a = int(input('=? First number: '))
b = int(input('=? Second number: '))
c = int(input('=? Third number: '))
print('=========')

r = (a + b) ** 2
s = (b + c) ** 2
d = (r + s) / 2

print(f'The expression equals: {d}')