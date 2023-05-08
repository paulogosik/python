width = float(input('=> What is the widht of the rectangle? '))
height = float(input('=> And what is the height of the rectangle? '))
print('----------------')

perimeter = (width * 2) + (height * 2)
area = width * height

print(f'=> The perimeter of the rectangle is: {perimeter:.1f}\n'
      f'=> The area of the rectangle is: {area:.1f}')