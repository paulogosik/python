import Tree

t = Tree.Tree()
t.insere(4)
t.insere(2)
t.insere(5)
t.insere(1)
#t.insere(3)
t.insere(10)
t.insere(11)
t.insere(7)
t.insere(6)
t.insere(9)
t.insere(8)

# Questão 1:
print('*')
t.nos_com_descendente_par()

# Questão 2:
print('**')
print(t.tem_descendente_par(10))
print(t.tem_descendente_par(2))

# Questão 3:
print('***')
t.imprime_maior_filho(2)
