exp = str(input(f"=> Type your math expression: "))
openExpr = 0
closeExpr = 0

for char in exp:
    if char == "(":
        openExpr += 1
    elif char == ")":
        closeExpr += 1

if openExpr == closeExpr:
    print(f"=> Your expression is valid!")
else:
    print(f"=> Your expression is NOT valid!")
