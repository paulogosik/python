velocidade = int(input('\033[30mVelocidade do carro:\033[m'))
acima = velocidade - 80
multa = acima * 7
if velocidade >80:
    print('\033[1;31mO seu carro passou do limite de velcidade! Você irá pagar R${:.2f} de multa\033[m!'.format(multa))
else:
    print('\033[32mParabéns! O seu carro está dentro do limite de velocidade!\033[m')