print(' ==={ NASCIMENTO DA PESSOA UM }===')
nome1 = input('=> Qual o nome da pessoa 1? ')
dia1 = int(input('=> Qual o dia do nascimento? '))
mes1 = int(input('=> Qual o mês do nascimento? '))
ano1 = int(input('=> Qual o ano do nascimento? '))
print('==============================')
print(' ==={ NASCIMENTO DA PESSOA DOIS }===')
nome2 = input('=> Qual o nome da pessoa 2? ')
dia2 = int(input('=> Qual o dia do nascimento? '))
mes2 = int(input('=> Qual o mês do nascimento? '))
ano2 = int(input('=> Qual o ano do nascimento? '))
print('==============================')
nome1 = nome1.capitalize()
nome2 = nome2.capitalize()

if ano1 < ano2:
    print(f'=> {nome1} é mais velho(a) que {nome2}.')
elif ano1 > ano2:
    print(f'=> {nome2} é mais velho(a) que {nome1}.')
else:
    if mes1 < mes2:
        print(f'=> {nome1} é mais velho(a) que {nome2}.')
    elif mes1 > mes2:
        print(f'=> {nome2} é mais velho(a) que {nome1}.')
    else:
        if dia1 < dia2:
            print(f'=> {nome1} é mais velho(a) que {nome2}.')
        elif dia1 > dia2:
            print(f'=> {nome2} é mais velho(a) que {nome1}.')
        else:
            print(f'=> {nome1} e {nome2} tem a mesma idade.')