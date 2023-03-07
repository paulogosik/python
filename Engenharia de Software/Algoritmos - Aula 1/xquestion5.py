print('=== Welcome to OurCompany ===')
name = input('=? What is your name, employee? ')
code = str(input('=? Whats is your code? '))
hours = int(input('=? How many hours did you work? '))
price = float(input('=? What was the value received per hour? '))
print('=========')

salary = hours * price

print(f'Employee: {name}\n'
      f'Code: #{code}\n'
      f'Salary: {salary}')