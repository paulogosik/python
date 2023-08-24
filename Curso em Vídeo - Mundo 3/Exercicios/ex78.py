nums = []
lowerNum = []
higherNum = []

for c in range(5):
    nums.append(int(input(f"=> Inform any integer number: ")))    
print(f"-" * 45)

for i, num in enumerate(nums):
    if i == 0:
        lowerNum.append(i)
        lowerNum.append(num)
        higherNum.append(i)
        higherNum.append(num)
    if num < lowerNum[1]:
        lowerNum[0] = i
        lowerNum[1] = num
    elif num > higherNum[1]:
        higherNum[0] = i
        higherNum[1] = num

print(f"=> The lowest number was {lowerNum[1]} in the {lowerNum[0] + 1}° place")
print(f"=> The highest number was: {higherNum[1]} in the {higherNum[0] + 1}° place")