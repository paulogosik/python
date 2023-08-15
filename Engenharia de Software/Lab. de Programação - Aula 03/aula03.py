meses = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")
print(meses)
print(len(meses))
print(meses[11])
print(meses[10:])

# LISTA ANINHADA---------------------------------------
print("\nLISTA ANINHADA ---------------------------")
a = ["p", "q", "r"]
b = ["t", a, "u"]

print(f"=> Tamanho de b: {len(b)}")
print(f"=> b: {b}")
print(f"=> b[1]: {b[1]}")
print(f"=> b[1][0]: {b[1][0]}")

# APPEND ---------------------------------------
print("\nAPPEND ---------------------------")
lista1 = ["a", "b", "c"]
print(f"=> lista1 antes do append: {lista1}")
lista1.append("f")
print(f"=> lista1 depois do append: {lista1}")

# EXTEND---------------------------------------
print("\nEXTEND ---------------------------")
lista1 = ["a", "b", "c"]
lista2 = ["d", "e"]
print(f"=> lista1 antes do extend: {lista1}")
lista1.extend(lista2)
print(f"=> lista1 depois do extend: {lista1}")

# INSERT ---------------------------------------
print("\nINSERT ---------------------------")
lista1 = ["a", "b", "c"]
print(f"=> lista1 antes do insert: {lista1}")
lista1.insert(2, "k")
print(f"=> lista1 depois do insert: {lista1}")

# REMOVE ---------------------------------------
print("\nREMOVE ---------------------------")
lista1 = ["a", "b", "c"]
print(f"=> lista1 antes do remove: {lista1}")
lista1.remove("b")
print(f"=> lista1 depois do remove: {lista1}")

# POP ---------------------------------------
print("\nPOP ---------------------------")
lista1 = ["a", "b", "c"]
print(f"=> lista1 antes do pop: {lista1}")
x = lista1.pop(1)
print(f"=> lista1 depois do pop: {lista1}")
print(f"=> Valor de x: {x}")

# SORT ---------------------------------------
print("\nSORT ---------------------------")
lista1 = ["x", "b", "v", "b"]
print(f"=> lista1 antes do sort: {lista1}")
x = lista1.sort()
print(f"=> lista1 depois do sort: {lista1}")