import random
valorAleatorio = random.randint(1, 10)

n1 = int(input('=> Digite um número inteiro: '))
print('-----------------')

if n1 > valorAleatorio:
    print('=> Usuário digitou um número maior!')
elif n1 == valorAleatorio:
    print('=> Usuário digitou um número igual!')
else:
    print('=> A máquina escolheu um número maior!')