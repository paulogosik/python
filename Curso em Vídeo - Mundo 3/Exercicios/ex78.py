nums = []
lowerNum = []
higherNum = []

for c in range(5):
    nums.append(int(input(f"=> Inform any integer number: ")))    
print(f"-" * 45)

for i, num in enumerate(nums):
    if i == 0:
        lowerNum = num
        higherNum = num
    if num < lowerNum:
        lowerNum = num
    elif num > higherNum:
        higherNum = num

print(f"=> The lowest number was {lowerNum} at the position(s): ", end='')
for i, num in enumerate(nums):
    if num == lowerNum:
        print(f"{i} ", end='')
print("")
print(f"=> The highest number was: {higherNum} at the position(s): ", end='')
for i, num in enumerate(nums):
    if num == higherNum:
        print(f"{i} ", end='')
print("")