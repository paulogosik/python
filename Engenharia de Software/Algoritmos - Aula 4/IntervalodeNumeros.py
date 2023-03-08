n1 = float(input('=> Me diga um número qualquer: '))
print('-------------------')

if n1 >= 10 and n1 <= 50:
    print(f'=> O número {n1} está entre 10 e 50!')
else:
    if n1 > 50:
        print(f'=> O número {n1} está acima do intervalo entre 10 e 50!')
    else:
        print(f'=> O número {n1} está abaixo do intervalo entre 10 e 50!')