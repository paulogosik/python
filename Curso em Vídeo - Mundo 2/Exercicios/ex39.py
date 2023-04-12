name = input('=> What is your name? ')
year = int(input('=> In which year were you born? '))
print('=========')

age = 2023 - year

if age > 18:
    time = age - 18
    print(f'=> You were already supposed to enlist, {name}!\n'
          f'=> Time past: {time} year(s).')
elif age < 18:
    time = 18 - age
    print(f'=> You will still enlist, {name}!\n'
          f'=> Time left: {time} year(s).')
else:
    print(f'=> You have to enlist this year, {name}!\n'
          f'=> Be aware on enlist dates.')