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

# -------------------------------------
print("-" * 30)
eu = {"nome": "Paulo Moita",
      "idade": 18,
      "sexo": "M"
      }
print(f"=> O {eu['nome']} tem {eu['idade']} anos.")

# -------------------------------------
print("-" * 30)
brasil = []
estado1 = {"UF": "Rio de Janeiro",
           "Sigla": "RJ"
           }
estado2 = {"UF": "São Paulo",
           "Sigla": "SP"
           }
brasil.append(estado1)
brasil.append(estado2)
print(f"Estado 1: {estado1}\n"
      f"Estado 2: {estado2}\n"
      f"Brasil: {brasil}")

# -------------------------------------
print("-" * 30)
estado = {}
estados = []
sigla = None
while sigla != "XX":
    sigla = input("Informe a sigla (\"XX\" para o código): ").upper()
    if sigla == "XX":
        break
    uf = input("Infomre a UF: ").title()
    estado["Sigla"] = sigla
    estado["UF"] = uf
    estados.append(estado.copy())
    estado.clear()

print("-" * 15)
for estado in estados:
    for key, value in estado.items():
        print(f"\t{key}: {value}")
        if key == "UF":
            print("")
print("-" * 15)
