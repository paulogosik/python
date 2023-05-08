nome = input('=> Qual o nome do vendedor? ')
nome = nome.capitalize()
salario = float(input('=> Qual o salário fixo do vendedor? '))
vendas = float(input('=> Qual foi o total de vendas feitas no mês? '))
print('------------------')

nsalario = (vendas *0.15) + salario

print(f'=> O salário de {nome} é R${nsalario:.2f}.')