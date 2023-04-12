nomeMaisCaro = ''
categoriaMaisBarata = ''
maiorPreco = 0
menorPreco = 0

preco = float(input("=> Informe o preço da obra: "))

while preco > 0:
    nome = input("=> Informe o nome do artista: ")
    print(f"=> Escolha uma das categorias para a obra.\n"
          f"=>      [E] Escultura\n"
          f"=>      [Q] Quadro")
    categoria = input("=> ")
    categoria = categoria.upper()
    
    if preco > maiorPreco and categoria == "E":
        maiorPreco = preco
        nomeMaisCaro = nome
    if menorPreco == 0:
        menorPreco = preco
        categoriaMaisBarata = categoria
    elif menorPreco > preco:
        menorPreco = preco
        categoriaMaisBarata = categoria
    
    print("-------------------------------")
    preco = float(input("=> Informe o preço da obra: "))

print("-------------------------------")
print(f"=> Artista com a escultura mais cara: {nomeMaisCaro} ")
if categoriaMaisBarata == "Q":
    categoriaMaisBarata = "Quadro"
elif categoriaMaisBarata == "E":
    categoriaMaisBarata = "Escultura"
print(f"=> Categoria da obra mais barata: {categoriaMaisBarata}")    