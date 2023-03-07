name = input('=> What is the name of the athlete? ')
born = int(input('=> What was the birth year? '))
print('---------')

age = 2023 - born

if age <= 9:
    print(f'=> Athlete: {name}\n'
          f'=> Category: MIRIM')
elif age > 9 and age <= 14:
    print(f'=> Athlete: {name}\n'
          f'=> Category: INFANTIL')
elif age > 14 and age <= 19:
    print(f'=> Athlete: {name}\n'
          f'=> Category: JUNIOR')
elif age == 20:
    print(f'=> Athlete: {name}\n'
          f'=> Category: SÊNIOR')
else:
    print(f'=> Athlete: {name}\n'
          f'=> Category: MASTER')