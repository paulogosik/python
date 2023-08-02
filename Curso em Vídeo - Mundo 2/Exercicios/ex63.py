n = int(input(f"=> Type any integer number: "))
i = 0
term1 = term2 = 1

while i < n:
    result = term1 + term2
    print(f"{term1} + {term2} = {result}")
    term2 = term1
    term1 = result
    
    i += 1