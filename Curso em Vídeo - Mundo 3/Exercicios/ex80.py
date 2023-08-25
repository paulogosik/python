list = []

for c in range(5):
    num = int(input(f"=> Inform any integer number: "))
    
    if (c == 0) or (num > list[len(list) - 1]):
        list.append(num)
        print(f"=> The number {num} was added at the final")
    elif num < list[0]:
        list.insert(0, num)
        print(f"=> The number {num} was added at the posiniton number 0")
    else:
        pos = 0
        while pos < len(list):
            if num <= list[pos]:
                list.insert(pos, num)
                print(f"=> The number {num} was added at the position number {pos}")
                break
            pos += 1    
print(f"-" * 45)
print(f"=> The list ordened is: {list}")