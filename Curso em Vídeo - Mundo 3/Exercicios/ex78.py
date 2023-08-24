nums = []
lowerNum = 0
higherNum = 0

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

print(f"=> The lowest number was: {lowerNum}")
print(f"=> The highest number was: {higherNum}")