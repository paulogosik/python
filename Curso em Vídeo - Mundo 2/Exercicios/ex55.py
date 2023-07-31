higherWeight = 0
lowerWeight = 0

for c in range(0, 5):
    weight = float(input(f"=> Inform your weight: "))
    
    if c == 0:
        higherWeight = weight
        lowerWeight = weight
    elif weight > higherWeight:
        higherWeight = weight
    elif weight < lowerWeight:
        lowerWeight = weight

print(f"---------------")
print(f"=> Lower weight: {lowerWeight}")
print(f"=> Higher weight: {higherWeight}")