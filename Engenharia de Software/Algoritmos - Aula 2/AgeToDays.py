years = int(input('=> What is your age (just in years)? '))
months = int(input('=> And the months? '))
days = int(input('=> And the days? '))
print('-------------------')

dYears = years * 365
dMonths = months * 30
fDays = dYears + dMonths + days

print(f'You have {fDays} days of life!')