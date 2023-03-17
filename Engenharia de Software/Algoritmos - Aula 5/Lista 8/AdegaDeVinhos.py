i = 0
contB = 0
contT = 0
contR = 0

while i < 15:
    i += 1
    print(f"=> Qual o tipo do vinho {i}?\n"
          f"    [B] - Branco\n"
          f"    [T] - Tinto\n"
          f"    [R] - Rosê")
    vinho = input("=> ")
    vinho = vinho.upper()

    if vinho == 'B':
        contB = contB + 1
    elif vinho == 'T':
        contT = contT + 1
    elif vinho == 'R':
        contR = contR + 1
    else:
        print(f"=> Opção ({vinho}) inválida.")
    
    print("---------------------------")

porcentB = (contB * 100) / 15
porcentT = (contT * 100) / 15
porcentR = (contR * 100) / 15

print(f"=> Percentual de vinho branco: %{porcentB:.2f}")
print(f"=> Percentual de vinho tinto: %{porcentT:.2f}")
print(f"=> Percentual de vinho rosê: %{porcentR:.2f}")