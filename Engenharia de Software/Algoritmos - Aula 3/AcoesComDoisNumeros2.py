n1 = float(input('=> Informe um número: '))
n2 = float(input('=> Informe outro número: '))
print('-----------------------')

if n1 != n2:
    if n1 < n2:
        dif = n2 - n1
        print(f'=> A diferença do maior pelo menos é: {dif}.')
    else:
        dif = n1 - n2
        print(f'=> A diferença do maior pelo menos é: {dif}.')
else: 
    soma = n1 + n2
    print(f'=> A soma dos números é: {soma}.')