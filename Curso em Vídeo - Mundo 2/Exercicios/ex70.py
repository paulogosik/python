totalSpent = quantExpensive = 0
nameCheaper = ''
priceCheaper = 0
print(f"=> DESCRIBE THE PRODUCTS YOU BOUGHT")

while True:
    name = input("=> What is the product? ")
    price = float(input("=> How much was it? $"))
    
    totalSpent += price
    
    if price > 1000:
        quantExpensive += 1
    if priceCheaper == 0:
        priceCheaper = price
        nameCheaper = name
    elif priceCheaper > price:
        priceCheaper = price
        nameCheaper = name
    
    option = input("=> Do you want to continue? [Y/N] ").upper()
    print(f"-----------------")
    if option == 'N':
        break

print(f"=> The total spent was ${totalSpent}")
print(f"=> {quantExpensive} products was more than $1000")
print(f"=> {nameCheaper} was the cheaper product and it was ${priceCheaper}")