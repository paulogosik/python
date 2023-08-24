nums = []
option = None

while option != "N":
    num = int(input(f"=> Type any integer number: "))
    
    if num not in nums:
        nums.append(num)
        print(f"=> Number added!")
    else:
        print(f"=> '{num}' already exists!")
    
    option = input(f"=> Do you want to continue? [Y/N] ").upper()
    print(f"-" * 45)

nums.sort()
print(f"=> You typed the numbers: {nums}")