from random import randint
numbers = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
lower = 0
higher = 0

for number in numbers:
    if lower == 0:
        lower = number
    if number < lower:
        lower = number
    if number > higher:
        higher = number
    
print(f"=> The numbers are: {numbers}")
print(f"=> The lower number is: {lower}")
print(f"=> The higher number is: {higher}")