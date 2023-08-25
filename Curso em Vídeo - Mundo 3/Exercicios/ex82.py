nums = []
evenNums = []
oddNums = []
option = None

while option != "N":
    num = int(input(f"=> Type any integer number: "))
    nums.append(num)
    
    option = input(f"=> Do you want to continue? [Y/N] ").upper()
    print(f"-" * 45)
    
for num in nums:
    if num % 2 == 0:
        evenNums.append(num)
    else:
        oddNums.append(num)
        
print(f"=> The whole list is: {nums}")
print(f"=> The list with even numbers is: {evenNums}")
print(f"=> The list with odd numbers is: {oddNums}")