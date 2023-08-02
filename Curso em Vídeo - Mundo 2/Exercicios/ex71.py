print("=> =[ WELCOME TO MY ATM ]=")

value = int(input(f"=> Type an integer value to withdraw. $"))
    
fifty = value // 50
rest = value % 50
twenty = rest // 20
rest = rest % 20
tens = rest // 10
rest = rest % 10
ones = rest

print(f"-----------------")
print(f"=> $50 notes: {fifty}")
print(f"=> $20 notes: {twenty}")
print(f"=> $10 notes: {tens}")
print(f"=> $1 notes: {ones}")
print(f"-----------------")
print(f"=> Thanks! You're always welcome.")