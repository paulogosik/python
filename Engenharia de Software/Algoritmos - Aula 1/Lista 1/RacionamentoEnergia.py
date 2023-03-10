salary = float(input('=? Hello, what is your salary? '))
quant = float(input('=? And how much energy you spend in your house in kilowatts? '))
print('')

cent = salary * 0.01
bill = cent * quant

print(f'=! Your salary is ${salary}, so, your bill will be {bill}!')