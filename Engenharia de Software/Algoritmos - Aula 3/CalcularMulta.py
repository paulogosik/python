veloM = float(input('=> Qual a velocidade máxima pertmitida na via? '))
veloC = float(input('=> Qual a velocidade do carro que passou por ela? '))
print('-------------------------')

if veloC <= veloM:
    print('=> Motorista dentro da velocidade permitida.')
else:
    multa = (veloC - veloM) * 10
    print(f'=> Motorista ultrapassou a velocidade máxima!\n'
          f'=> Valor da multa: R${multa}')