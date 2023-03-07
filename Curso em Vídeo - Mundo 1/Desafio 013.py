print('Houve um reajuste de 15% salarial, e esse programa calcula quanto ficará o salário novo com o reajuste.')
salário = float(input('Salário antigo: R$'))
novo = salário + (salário * 15 / 100)
print('O seu novo salário será de: R${}'.format(novo))
