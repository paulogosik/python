# Levando em conta 'x' sendo o número de caracteres da linha:
    # :^'x' - USADO PARA CENTRALIZAR
    # :<'x' - USADO PARA ALINHAR A DIREITA
    # :>'x' - USADO PARA ALINHAR A ESQUERDA

products = ("Mouse", 80.0, "Keyboard", 199.90, "Monitor", 499.9, "MacBook", 999.8, "iPhone", 899.9)

print(f"-" * 38)
print(f"{'LISTAGEM DE PREÇOS':^38}")
print(f"-" * 38)

for i in range(0, len(products), 2):
    print(f"{products[i]:.<30}", end='')
    print(f"U${products[i + 1]:>6}")
print(f"-" * 38)