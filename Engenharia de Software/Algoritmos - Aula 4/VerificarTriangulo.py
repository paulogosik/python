a = float(input('=> Informe o lado A de um triângulo: '))
b = float(input('=> Informe o lado B de um triângulo: '))
c = float(input('=> Informe o lado C de um triângulo: '))
print('-----------------')

if (a < (b + c)) and (b < (a + c)) and (c < (a + b)):
    print('=> Podem ser lados de um triângulos!')
    if a == b == c:
        print('=> Triângulo equilátero!')
    elif (a == b != c) or (a == c != b) or (b == c != a):
        print('=> Triângulo isóceles!')
    else:
        print('=> Triângulo escaleno!')
else:
    print('=> Não podem ser lados de um triângulos!')