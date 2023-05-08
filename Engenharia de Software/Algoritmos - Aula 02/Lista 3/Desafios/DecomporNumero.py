num = int(input('=> Digite um número inteiro: '))
print('--------------------')

centena = num // 100
dezena = (num - (centena * 100)) // 10
unidade = num - ((centena * 100) + (dezena * 10))

print(f'=> {centena} centena(s), {dezena} dezena(s) e {unidade} unidade(s).')