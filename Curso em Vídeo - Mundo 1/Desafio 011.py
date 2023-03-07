print('Esse programa irá dizer quantos litros de tinta você precisa para pintar a sua parede utilizando a sua dimensão.')
alt = float(input('Altura da parede:'))
lar = float(input('Largura da parede:'))
area = alt * lar
tinta = area / 2
print('Sua parede tem dimensões de {}m x {}m. A sua área é de {} metros quadrados.'.format(alt, lar, area))
print('Sendo assim você precisará de {} litros de tinta para pintar a sua parede!'.format(tinta))