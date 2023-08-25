nums = []
option = None

while option != "N":
    num = int(input(f"=> Type any integer number: "))
    nums.append(num)
    
    option = input(f"=> Do you want to continue? [Y/N] ").upper()
    print(f"-" * 45)
    
print(f"=> You typed {len(nums)} numbers.")
nums.sort(reverse = True)
print(f"=> The numbers in the descending order is: {nums}")

if 5 in nums:
    print(f"=> The number 5 is actually in the list.")
else:
    print(f"=> The number 5 is not in the list.")