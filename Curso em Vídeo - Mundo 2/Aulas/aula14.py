# A estrutura de repetição 'for' é usada quando temos a quantidade de vezes que será repetida
# Já a estrutura de repetição 'while' é quando não sabemos a quantidade

n = 1
evens = odds = 0

while n != 0:
    n = int(input(f"=> Type any number: "))
    
    if n != 0:
        if n % 2 == 0:
            evens += 1
        else:
            odds += 1
    
print(f"--------------")
print(f"=> {evens} numbers were even")
print(f"=> {odds} numbers were odd")