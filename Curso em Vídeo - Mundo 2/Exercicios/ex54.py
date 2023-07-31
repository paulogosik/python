legalAge = 0
minor = 0

for c in range(0, 7):
    yy = int(input("=> What year were you born? "))
    if (2023 - yy) >= 21:
        legalAge += 1
    else:
        minor += 1
        
print(f"-----------------")
print(f"=> The number of people of legal age is: {legalAge}")
print(f"=> The number of minors is: {minor}")