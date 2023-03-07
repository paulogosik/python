name = str(input('=> Hello, welcome to OurCompany! What is your name: '))
hvalue = float(input('=> What is the value of the house? '))
salary = float(input('=> What is your salary? '))
years = float(input('=> And, in how many years will you pay the house? '))
print('=========')

months = years * 12
portion = hvalue / months
salaryp = salary * 0.3

if salaryp > portion:
    print('APPROVED');
    print(f'=>Congratulations, {name}! The provision of the house will be ${portion:.2f} and you can afford it!\n'
          f'Good to have you with OurCompany, {name}!')
else:
    print('DENIED!');
    print(f'I am sorry, {name}. The provision of the house will be ${portion:.2f} and 30% of your salary is: ${salaryp:.2f}.'
          f'Have a good day!')