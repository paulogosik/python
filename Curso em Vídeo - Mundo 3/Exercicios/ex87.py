matrix = [[], [], []]
totalEvenSum = highestNum = thirdColumn = 0

for i in range(3):
    for c in range(3):
        num = int(input(f"=> Type the a number to [{i}, {c}]: "))
        matrix[i].append(num)

        if num % 2 == 0:
            totalEvenSum += num
        if c == 2:
            thirdColumn += num

print("-" * 30)
for i in range(3):
    print(f"[ {matrix[i][0]} ] [ {matrix[i][1]} ] [ {matrix[i][2]} ]")

for num in matrix[1]:
    if num > highestNum:
        highestNum = num

print("-" * 30)
print(f"=> The total sum of the numbers is: {totalEvenSum}")
print(f"=> The sum of the third column is: {thirdColumn}")
print(f"=> The highest number of the second column is: {highestNum}")
