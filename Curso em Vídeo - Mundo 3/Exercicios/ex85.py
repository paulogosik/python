generalList = [[], []]
evenNumbers = []
oddNumbers = []

for i in range(7):
    num = int(input(f"=> Type the {i + 1}° number: "))
    if num % 2 == 0:
        generalList[0].append(num)
    else:
        generalList[1].append(num)

print("-" * 30)
generalList[0].sort()
generalList[1].sort()
evenNumbers = generalList[0][:]
oddNumbers = generalList[1][:]

print(f"=> The typed even numbers was: {evenNumbers}")
print(f"=> The typed odd numbers was: {oddNumbers}")
