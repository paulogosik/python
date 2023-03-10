distance = float(input('=> What is the distance between the origin city and the destiny city? '))
valueFuel = float(input('=> What is the value of the fuel? '))
consumption = float(input('=> What is the consumption of your car? '))
print('----------------------')

authonomy = distance / consumption
spent = authonomy * valueFuel

print(f'=> You will spend ${spent:.2f} on your trip!')