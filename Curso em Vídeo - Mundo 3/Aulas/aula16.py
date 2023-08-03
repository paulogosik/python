# # PARTE TEÓRICA -----------------------------------------------
# var = '0 - hamburger', '1 - soda', '2 - pizza', '3 - cake'
# # Da o print em todos os elementos da Tupla;
# print(var)

# # O índice é indicado e é impresso somente ele;
# print(var[2])

# # Indica o intervalo da Tupla, o último [2, por exemplo] não será impresso;
# print(var[0:2])

# # Imprime o valor indicado em diante;
# print(var[1:])

# # Imprime o último valor e esta contagem é seguida de trás para frente;
# print(var[-1])

# # Imprime a quantidade de registros dentro da Tupla;
# print(len(var))

# # A variável c se torna uma variável simples que é a tupla[c];
# for c in var:
#     print(c)

# PARTE PRÁTICA -----------------------------------------------
lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
print(lanche[:7])

print(f"----------------------")

for c in lanche:
    print(f"=> Eu vou comer {c}")

print(f"----------------------")

for c in enumerate(lanche):
    print(c)
    print(f"=> {c[0]} - Eu vou comer {c[1]}")