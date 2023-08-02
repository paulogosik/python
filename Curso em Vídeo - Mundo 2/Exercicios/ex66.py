c = 0
sumN = 0

while True:
    num = int(input(f"=> Type any integer number [999 to stop]: "))
    if num == 999:
        break
    
    c += 1
    sumN += num

print("------------")
print(f"=> The sum of the {c} numbers is: {sumN}")