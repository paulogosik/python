n1 = float(input('=> Digite um número: '))
n2 = float(input('=> Digite outro número: '))
print('=> Digite uma das opções abaixo:\n'
      '     [c] Ordem crescente\n'
      '     [d] Ordem decrescente')
opcao = input('=> Digite sua escolha: ')
print('---------------')

if opcao == 'c':
    if n1 > n2:
        print(f'=> Ordem crescente: {n2} e {n1}!')
    elif n2 > n1:
        print(f'=> Ordem crescente: {n1} e {n2}!')
    else:
        print('=> Números iguais!')
elif opcao == 'd':
    if n1 > n2:
        print(f'=> Ordem decrescente: {n1} e {n2}!')
    elif n2 > n1:
        print(f'=> Ordem decrescente: {n2} e {n1}!')
    else:
        print('=> Números iguais!')
else:
    print('=> Opção indisponível!')