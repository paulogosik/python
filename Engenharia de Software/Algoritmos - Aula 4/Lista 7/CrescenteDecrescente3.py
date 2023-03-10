n1 = int(input('=> Digite um valor: '))
n2 = int(input('=> Digite outro valor: '))
n3 = int(input('=> Digite outro valor: '))
op = input('=> Digite "C" para ordem crescente ou "D" para ordem decrescente: ')
op = op.upper()
print('------------------------')

if n1 == n2 == n3:
    print('=> Os números são iguais!')
elif n1 == n2 or n1 == n3 or n2 == n3:
    print('=> Algum número tem o mesmo valor de outro!')
else: 
    if op == 'C':
        if n1 < n2 < n3:
            print(f'=> A ordem crescente é: {n1}, {n2} e {n3}.')
        elif n1 < n3 < n2:
            print(f'=> A ordem crescente é: {n1}, {n3} e {n2}.')
        elif n2 < n1 < n3:
            print(f'=> A ordem crescente é: {n2}, {n1} e {n3}.')
        elif n2 < n3 < n1:
            print(f'=> A ordem crescente é: {n2}, {n3} e {n1}.')
        elif n3 < n1 < n2:
            print(f'=> A ordem crescente é: {n3}, {n1} e {n2}.')
        elif n3 < n2 < n1:
            print(f'=> A ordem crescente é: {n3}, {n2} e {n1}.')
    elif op == 'D':
        if n1 > n2 > n3:
            print(f'=> A ordem decrescente é: {n1}, {n2} e {n3}.')
        elif n1 > n3 > n2:
            print(f'=> A ordem decrescente é: {n1}, {n3} e {n2}.')
        elif n2 > n1 > n3:
            print(f'=> A ordem decrescente é: {n2}, {n1} e {n3}.')
        elif n2 > n3 > n1:
            print(f'=> A ordem decrescente é: {n2}, {n3} e {n1}.')
        elif n3 > n1 > n2:
            print(f'=> A ordem decrescente é: {n3}, {n1} e {n2}.')
        elif n3 > n2 > n1:
            print(f'=> A ordem decrescente é: {n3}, {n2} e {n1}.')
    else:
        print('=> Opção indisponível.')