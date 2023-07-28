sum = 0

for c in range(1, 500):
    if (c % 2 != 0) and (c % 3 == 0):
        sum += c

print(f"=> The sum of all the odd divisible by three numbers is: {sum}")