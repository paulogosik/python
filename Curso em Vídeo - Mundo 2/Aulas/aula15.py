# Usamos o 'break' para poder quebrar e parar o laço de repetição a qualquer momento

n = sumN = 0
while True:
    n = int(input(f"=> Type any number: "))
    sumN += n
    
    if sumN > 15:
        break
print(f"=> The sum of the numbers is: {sumN}")