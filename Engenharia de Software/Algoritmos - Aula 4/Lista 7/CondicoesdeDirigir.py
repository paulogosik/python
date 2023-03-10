print(' ==={ RESPONDA "S" PARA SIM OU "N" PARA NÃO }=== ')
cinto = input('=> Você está usando cinto de sgurnaça? ')
cinto = cinto.upper()
sobrio = input('=> Você está sóbrio? ')
sobrio = sobrio.upper()
revisao = input('=> O carro está com a revisão em dia? ')
revisao= revisao.upper()
print('-----------------------')

if cinto == 'N' or sobrio == 'N' or revisao == 'N':
    print('=> Você não está em condição de dirigir com segurança!')
else:
    print('=> Boa viagem!')