total = 0
num = int(input(f"=> Type any integer number ['999' to exit]: "))

while num != 999:
    total += num
    num = int(input(f"=> Type any integer number ['999' to exit]: "))

print(f"=> The result of the sum is: {total}")