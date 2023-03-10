salary = float(input('=? Hello, João, what is your salary? '))
bill1 = float(input('=? How much is the first bill? '))
bill2 = float(input('=? How much is the second bill? '))
print('=========')

tax1 = bill1 * 0.02
tax2 = bill2 * 0.02
fbill1 = bill1 + tax1
fbill2 = bill2 + tax2
fsalary = salary - (fbill1 + fbill2)

print(f'=> The taxes of the first bill was ${tax1} and you payed ${fbill1}.\n'
      f'=> The taxes of the second bill was ${tax2} and you payed ${fbill2}.\n'
      f'=> You have ${fsalary} left of your salary.')