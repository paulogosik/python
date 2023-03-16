i = 0
iS = 0
iN = 0
c = int(input("=> Quantas pessoas estavam no teatro? "))

while i < c:
    i += 1
    valid = input(f"=> Pessoa {i}, você gostou da apresentação? Digite 'S' para sim ou 'N' para não. ")
    print('------------------------------')
    valid = valid.upper()

    if valid == 'S':
        iS += 1
    elif valid == 'N':
        iN += 1

if iS > iN:
    print(f"=> A maioria das pessoas gostaram da apresentação.\n"
           f"=> Sim: {iS}\n"
           f"=> Não: {iN}")
elif iN > iS:
    print(f"=> A maioria das pessoas não gostaram da apresentação.\n"
           f"=> Sim: {iS}\n"
           f"=> Não: {iN}")
else:
    print(f"=> O número de pessoas que gostaram e não gostaram foi igual.\n"
           f"=> Sim: {iS}\n"
           f"=> Não: {iN}")