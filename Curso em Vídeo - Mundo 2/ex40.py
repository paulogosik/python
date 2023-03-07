name = input('=> What is the name of the student? ')
n1 = float(input('=> What was the first grade? '))
n2 = float(input('=> And what was the second grade? '))
print('=========')

average = (n1 + n2) / 2

if average < 5:
    print(f'=> Student: {name}\n'
          f'=> Average: {average}\n'
          f'=> Situation: FAIL')
elif average >= 7:
    print(f'=> Student: {name}\n'
          f'=> Average: {average}\n'
          f'=> Situation: APPROVED')
else:
    print(f'=> Student: {name}\n'
          f'=> Average: {average}\n'
          f'=> Situation: IN RECOVERY')