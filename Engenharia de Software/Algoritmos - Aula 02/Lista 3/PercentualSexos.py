women = int(input('=> What is the numbers of women in your class? '))
men = int(input('=> What is the numbers of men in your class? '))
print('---------------------')

total = women + men
pWomen = (women * 100) / total
pMen = (men * 100) / total

print(f'=> The total of people equals: {total:.2f}%\n'
      f'=> The percentage of women equals: {pWomen:.2f}%\n'
      f'=> The percentage of men equals: {pMen:.2f}%')