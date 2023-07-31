n1 = float(input(f"=> Type any number: "))
n2 = float(input(f"=> Type any number: "))
print("--------------")

opc = 0
while opc != 5:
    print("=> Choose one of the options below:\n"
        "     [1]Sum\n"
        "     [2]Multiplication\n"
        "     [3]Higher\n"
        "     [4]New numbers\n"
        "     [5]Exit the program")
    opc = int(input(f"=> "))
    print("--------------")
    
    if opc == 1:
        print(f"=> The sum between the numbers equals: {n1 + n2}")
        print("--------------")
        
    elif opc == 2:
        print(f"=> The multiplication between the numbers equals: {n1 * n2}")
        print("--------------")
        
    elif opc == 3:
        if n1 > n2:
            print(f"=> {n1} is higher than {n2}")
        elif n2 > n1:
            print(f"=> {n2} is higher than {n1}")
        elif n1 == n2:
            print(f"=> The numbers are the same")
        print("--------------")
        
    elif opc == 4:
        n1 = float(input(f"=> Type any number: "))
        n2 = float(input(f"=> Type any number: "))
        print("--------------")