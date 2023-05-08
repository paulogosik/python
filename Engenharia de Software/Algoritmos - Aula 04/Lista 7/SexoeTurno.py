print('Escolha uma das opções abaixo:\n'
      ' [M] Masculino\n'
      ' [F] Feminino')
sexo = input('=> ')
sexo = sexo.upper()
print('Escolha uma das opções abaixo:\n'
      ' [M] Matutino\n'
      ' [V] Vespertino')
turno = input('=> ')
turno = turno.upper()
print('-----------------')

if sexo == 'M' and turno == 'M':
    print('=> Bom dia, querido!')
elif sexo == 'M' and turno == 'V':
    print('=> Boa tarde, querido!')
elif sexo == 'F' and turno == 'M':
    print('=> Bom dia, querida!')
elif sexo == 'F' and turno == 'V':
    print('=> Boa tarde, querida!')
else:
    print('=> Opção Inválida!')