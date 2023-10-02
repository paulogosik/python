from ex2_funcoes import *

palavra = input("Informe uma palavra: ").title()
print("-" * 30)

# Questão A)
pos = 2
print(f"A letra na {pos}° posição da palavra [{palavra}] é: {naPosicao(palavra, pos)}")
pos = 6
print(f"A letra na {pos}° posição da palavra [{palavra}] é: {naPosicao(palavra, pos)}")
print("-" * 30)

# Questão B)
print(f"As posições de [a] na palavra [{palavra}]:")
posicoes(palavra, "a")
print("-" * 30)

# Questão C)
print(f"A palavra [{palavra}] começa com R? {iniciaCom(palavra, 'R')}")
print(f"A palavra [{palavra}] começa com C? {iniciaCom(palavra, 'C')}")
print("-" * 30)

# Questão D)
lista = ["Cavalo", "Teste", "Lagarto", "Fazenda"]
print(lista)
print(f"=> A maior palavra da lista é: {maiorPalavra(lista)}")
print("-" * 30)

# Questão E)
print(f"A palavra [{palavra}] é um conector? {ehConector(palavra)}")
print(f"A palavra [dos] é um conector? {ehConector('dos')}")
