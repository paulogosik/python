higher = 0
lower = 0
c = 0
totalNum = 0
option = 'Y'

while option == 'Y':
    num = int(input(f"=> Type an integer number: "))
    c += 1
    totalNum += num
    
    if lower == 0:
        lower = num
    elif lower > num:
        lower = num
    elif higher < num:
        higher = num
    
    option = input(f"=> Do you want to continue? [Y/N] ").upper()
    print(f"---------------")
    
print(f"=> The average of the number equals: {totalNum / c}")
print(f"=> The higher number is: {higher}")
print(f"=> The lower number is: {lower}")