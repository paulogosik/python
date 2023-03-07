print('=> Olá, qual o seu tipo de conta?\n'
      '     [R] Residencial\n'
      '     [C] Comercial\n'
      '     [I] Industrial')
conta = input('=> Escolha uma opção: ')
consumo = float(input('=> Qual o seu consumo de água em metros cúbicos? '))
conta = conta.upper()
print('-------------------------')

if conta == 'R':
    gasto = ((consumo - 100) * 0.05) + 5
    print(f'=> A sua conta de água para {consumo} metros cúbicos será de R${gasto:.2f}.')
elif conta == 'C':
    if consumo <= 80:
        gasto = 500
        print(f'=> A sua conta de água para {consumo} metros cúbicos será de R${gasto:.2f}.')
    else:
        gasto = ((consumo - 100) * 0.25) + 500
        print(f'=> A sua conta de água para {consumo} metros cúbicos será de R${gasto:.2f}.')
elif conta == 'I':
    if consumo <= 100:
        gasto = 800
        print(f'=> A sua conta de água para {consumo} metros cúbicos será de R${gasto:.2f}.')
    else: 
        gasto = ((consumo - 100) * 0.04) + 800
        print(f'=> A sua conta de água para {consumo} metros cúbicos será de R${gasto:.2f}.')
else:
    print('=> OPÇÃO INDISPONÍVEL')
