# # AULA 17 - LISTAS ---------------------------------------------
# # Parte teórica ---------------------------------------------
# lanche = ['hamburguer', 'suco', 'pizza', 'pudim']
# print(f"=> Lista [Original]: {lanche}")

# lanche[3] = 'picolé' # Trocar índice específica
# print(f"=> Lista [Lanche[3]]: {lanche}")

# lanche.append('cookie') # Adicionar ao final
# print(f"=> Lista [append]: {lanche}")

# lanche.insert(0, 'cachorro quente') # Adicionar em índice específico
# print(f"=> Lista [insert]: {lanche}")

# # Formas de apagar elementos:
#     # del lanche[3]
#     # lanche.pop(3)
#     # lanche.remove('pizza')

# lanche.pop() # pop() sem índice remove o último valor
# print(f"=> Lanche [pop]: {lanche}")

# # Criar lista com range() ---------------------------------------------
# print(f"-" * 60)
# valores = list(range(0, 10)) # Criando com range()
# print(f"=> Criando valores: {valores}")

# valores = [8, 2, 5, 4, 9, 3, 0]
# print(f"=> Novos valores: {valores}")
# valores.sort() # Organizando lista em ordem crescente
# print(f"=> Valores [sort]: {valores}")

# valores.sort(reverse = True) # Organiza em ordem decrescente
# print(f"=> Valores [sort(reverse)]: {valores}")

# Parte prática ---------------------------------------------
num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort()
print(num)
print(f"=> A lista 'num' tem {len(num)} elementos.")
num.insert(2, 2)
print(num)
num.remove(2)
print(num)

if 4 in num:
    num.remove(4)
else:
    print(f"=> O valor 4 não existe na lista")
    
print(f"-" * 50)
    
for c, v in enumerate(num):
    print(f"=> Na posição {c} encontrei o valor {v}")