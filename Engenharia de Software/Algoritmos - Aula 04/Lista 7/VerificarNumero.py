ni = int(input('=> Digite um valor inteiro: '))
print('------------------')

if (ni % 2 == 0) and (ni > 0):
    div = ni / 2
    print(f'=> A metade desse número é: {div:.1f}')
else:
    multi = ni * 2
    print(f'=> O dobro desse número é: {multi}')