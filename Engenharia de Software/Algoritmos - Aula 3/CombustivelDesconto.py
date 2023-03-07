quant = float(input('=> Quantos litros de combustível você colocou? '))
print('=> Escolha a opção de combustível que você adquiriu:\n'
      '     [A] Álcool\n'
      '     [G] Gasolina')
tipo = input('=> Digite uma opção: ')
tipo = tipo.upper()
print('--------------------')

if tipo == 'A':
    if quant >= 20 and quant <= 30:
        preco = quant * 5
        disconto = preco * 0.05
        novopreco = preco - disconto
        print(f'=> O preço de álcool para {quant} litros é R${novopreco:.2f}.')
    elif quant > 30:
        preco = quant * 5
        disconto = preco * 0.10
        novopreco = preco - disconto
        print(f'=> O preço de álcool para {quant} litros é R${novopreco:.2f}.')
    else:
        preco = quant * 5
        print(f'=> O preço de álcool para {quant} litros é R${preco:.2f}.')
elif tipo == 'G':
    if quant >= 20 and quant <= 30:
        preco = quant * 7
        disconto = preco * 0.05
        novopreco = preco - disconto
        print(f'=> O preço de gasolina para {quant} litros é R${novopreco:.2f}.')
    elif quant > 30:
        preco = quant * 7
        disconto = preco * 0.10
        novopreco = preco - disconto
        print(f'=> O preço de gasolina para {quant} litros é R${novopreco:.2f}.')
    else:
        preco = quant * 7
        print(f'=> O preço de gasolina para {quant} litros é R${preco:.2f}.')
else:
    print('=> OPÇÃO INDISPONÍVEL!')