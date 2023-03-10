import math
sala1 = int(input('=> Quantas crianças tem na primeira sala? '))
sala2 = int(input('=> Quantas crianças tem na segunda sala? '))
sala3 = int(input('=> Quantas crianças tem na terceira sala? '))    

totalC = sala1 + sala2 + sala3

div = totalC / 4
leite = math.ceil(div)
preco = leite * 3.5

print(f'=> Total de crianças: {totalC}\n'
      f'=> Qt. de litros de leite: {leite}\n'
      f'=> Custo: R${preco}')