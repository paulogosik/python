num = int(input(f"=> Choose a random number: "))
i = num
fact = 1

while i > 0:
    fact *= i
    i -= 1

print(f"=> The factorial number of {num}! is {fact}")