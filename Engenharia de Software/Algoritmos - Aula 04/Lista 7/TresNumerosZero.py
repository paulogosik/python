n1 = float(input('=> Digite um valor qualquer: '))
n2 = float(input('=> Digite outro valor qualquer: '))
n3 = float(input('=> Digite outro valor qualquer: '))
print('------------------')

if n1 != 0 and n2 != 0 and n3 != 0: #TODOS OS NÚMEROS DIFERENTES DE ZERO
    print('=> Todos os números são diferentes de zero!')
    if n1 > 0 and n2 > 0 and n3 > 0: #TODOS OS NÚMEROS POSITIVOS
        produto = n1 * n2 * n3
        print(f'=> O produto dos números é: {produto}!')
    elif (n1 > 0) or (n2 > 0) or (n3 > 0): #PELO MENOS UM NÚMERO POSITIVO
        soma = n1 + n2 + n3
        print(f'=> A soma dos números é: {soma}!')
    else: #TODOS OS NÚMEROS NEGATIVOS
        media = (n1 + n2 + n3) / 3
        print(f'=> A média dos números é: {media:.2f}!')
elif n1 != 0 or n2 != 0 or n3 != 0: #NEM TODOS SÃO DIFERENTES DE ZERO
    print('=> Nem todos os números são diferentes de zero!')
    if n1 == 0: #QUANDO N1 É ZERO
        if n2 == 0 or n3 == 0: #SE OUTRO NÚMERO FOR ZERO: DOIS ZEROS
            print('=> Dois números iguais a zero!')
        elif n2 != 0 and n3 !=0: #SE NENHUM OUTRO NÚMERO FOR ZERO: UM ZERO
            print('=> Um número igual a zero!')
    elif n2 == 0: #QUANDO N2 É ZERO
        if n1 == 0 or n3 == 0: 
            print('=> Dois números iguais a zero!')
        elif n1 != 0 and n3 !=0: 
            print('=> Um número igual a zero!')
    else: #QUANDO N3 É ZERO
        if n1 == 0 or n2 == 0: 
            print('=> Dois números iguais a zero!')
        elif n1 != 0 and n2 !=0:
            print('=> Um número igual a zero!')
else: #TRÊS NÚMEROS IGUAIS A ZERO
    print('=> Nem todos os números são diferentes de zero!')
    print('=> Três números iguais a zero!')
