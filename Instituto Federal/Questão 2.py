x = int(input('Diga um valor X:'))
y = int(input('Diga um valor y:'))
if y > 0 or y < 0:
    result = x / y
    print('A divisão de "{0}" por "{1}" é "{2}"!:'.format(x, y, result))
else:
    print('Divisão Impossível!')