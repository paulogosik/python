# PRIMEIRO PEDIDO AO USUÁRIO
print('=> Olá, me dê características de um animal que eu vou adivinhar!\n'
      '     [ Vertebrado ]\n'
      '     [ Invertebrado ]')
op1 = input('=> Escolha uma das opções acima: ')
op1 = op1.capitalize()
print('----------------------')

# SEGUNDO PEDIDO AO USUÁRIO
print('=> Olá, me dê características de um animal que eu vou adivinhar!\n'
      '  # Para Vertebrado!\n'
      '     [ Ave ]\n'
      '     [ Mamífero ]\n'
      '  # Para Invertebrado!\n'
      '     [ Inseto ]\n'
      '     [ Analídeo ]')
op2 = input('=> Escolha uma das opções acima: ')
op2 = op2.capitalize()
print('----------------------')

# TERCEIRO PEDIDO AO USUÁRIO
print('=> Olá, me dê características de um animal que eu vou adivinhar!\n'
      '     # Para Ave - [ Carnívoro ] ou [ Onívoro ]\n'
      '     # Para Mamífero - [ Onívoro ] ou [ Herbívoro ]\n'
      '     # Para Inseto - [ Hematófago ] ou [ Herbívoro ]\n'
      '     # Para Anelídeo - [ Hematófago ] ou [ Onívoro ]')
op3 = input('=> Escolha uma das opções acima: ')
op3 = op3.capitalize()
print('----------------------')

if op1 == 'Vertebrado':
    if op2 == 'Ave' and op3 == 'Carnivoro':
        print('=> Seu animal é uma Águia!')
    elif op2 == 'Ave' and op3 == 'Onivoro':
        print('=> Seu animal é uma Pombo!')
    elif op2 == 'Mamifero' and op3 == 'Onivoro':
        print('=> Seu animal é uma Homem!')
    elif op2 == 'Mamifero' and op3 == 'Herbivoro':
        print('=> Seu animal é uma Vaca!')

elif op1 == 'Invertebrado':
    if op2 == 'Inseto' and op3 == 'Hematofago':
        print('=> Seu animal é uma Pulga!')
    elif op2 == 'Inseto' and op3 == 'Herbivoro':
        print('=> Seu animal é uma Lagarta!')
    elif op2 == 'Analideo' and op3 == 'Hematofago':
        print('=> Seu animal é uma Sanguessuga!')
    elif op2 == 'Analideo' and op3 == 'Onivoro':
        print('=> Seu animal é uma Minhoca!')

else:
    print('=> OPÇÕES INVÁLIDAS')