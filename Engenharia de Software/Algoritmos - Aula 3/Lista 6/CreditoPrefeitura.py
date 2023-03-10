salario = float(input('=> Informe o seu salário bruto: '))
prestacao = float(input('=> Informe o valor previsto para a prestação: '))
print('-----------------------------')

valorm = salario * 0.3

if prestacao > valorm:
    print(f'=> O empréstimo não pode ser concebido!')
else:
    print('=> O empréstimo poderá ser concebido!')