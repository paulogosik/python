print('Eu vou calcular o desconto de 5% no preço do seu produto.')
preço = float(input('Preço do seu produto: R$'))
pc = preço * 5 / 100
desconto = preço - pc
print('O seu produto custando R${}. O desconto sendo R${}. O preço final fica: R${}.'.format(preço, pc, desconto))