# Aula 19 - Dicionários
#   Dicionários são identificados por {}
dados = {'nome': "Paulo", 'idade': 18}
print(f"=> Nome: {dados['nome']} | Idade: {dados['idade']}")

# Adicionar elementos (append não funciona)
dados['sexo'] = "M"
print(f"=> Dados depois de adicionados: {dados}")

# Remover elementos
del dados['idade']
print(f"=> Dados depois de removidos: {dados}")

# -------------------------------------
print("-" * 30)
filme = {'Titulo': "Star Wars",
         'Ano': 1977,
         'Diretor': "George Lucas"
         }

print(filme.values())
print(filme.keys())
print(filme.items())

print("-" * 30)
for key, value in filme.items():
    print(f"{key} -> {value}")

print("-" * 30)
for value in filme.values():
    print(f"Value: {value}")

print("-" * 30)
for key in filme.keys():
    print(f"Key: {key}")

print("-" * 30)
for item in filme.items():
    print(f"Item: {item}")
