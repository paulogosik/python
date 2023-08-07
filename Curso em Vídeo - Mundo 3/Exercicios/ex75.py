num1 = int(input(f"=> Inform a number: "))
num2 = int(input(f"=> Inform another number: "))
num3 = int(input(f"=> Inform another number: "))
num4 = int(input(f"=> Inform just one more number: "))
print(f"------------------")

numbers = (num1, num2, num3, num4)

nines = 0
for number in numbers:
    if number == 9:
        nines += 1
        
print(f"=> You typed the values: {numbers}")
print(f"=> The value 9 appeared {nines} times")
if num1 != 3 and num2 != 3 and num3 != 3 and num4 != 3:
    print(f"=> The number 3 was not typed in any position")
else:
    print(f"=> The number 3 was first typed at the {numbers.index(3) + 1} position")
print(f"=> The evens numbers are: ", end='')
for number in numbers:
    if number % 2 == 0:
        print(f"{number} ", end='')