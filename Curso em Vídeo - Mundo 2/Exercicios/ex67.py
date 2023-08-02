while True:
    num = int(input(f"=> Type an integer number: "))
    
    if num < 0:
        break
    
    i = 1
    print(f"--------------")
    while i <= 10:
        print(f"=> {num} x {i} = {num * i}")
        i += 1
    print(f"--------------")