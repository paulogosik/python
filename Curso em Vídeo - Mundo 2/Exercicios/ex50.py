sum = 0

for c in range(0, 6):
    num = int(input(f"=> Inform any integer number: "))
    if num % 2 == 0:
        sum += num

print("------------------------------")
print(f"=> The sum of the even numbers equals: {sum}")