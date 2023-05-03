totalPagamento = 0
nomeVendedorMenor = ""
menorNumeroCamisetas = 999999

salarioMinimo = float(input("=> Informe o valor do salário mínimo: "))
nome = input("=> Informe o nome do vendedor: ")
nome = nome.capitalize()

while nome != "Sair":
    numeroCamisetas = float(input("=> Informe o número de camisetas vendidas: "))
    print("---------------------------")
    
    valorTotal = salarioMinimo + (numeroCamisetas * 0.5)
    totalPagamento += valorTotal
    print(f"=> Nome do vendedor: {nome}")
    print(f"=> Valor recebido: R${valorTotal}")
    
    if valorTotal <= 1000:
        print(f"=> Categoria: A")
    elif valorTotal > 1000 and valorTotal <= 1500:
        print(f"=> Categoria: B")
    elif valorTotal > 1500 and valorTotal <= 2000:
        print(f"=> Categoria: C")
    elif valorTotal > 2000:
        print(f"=> Categoria: D")
        
    if numeroCamisetas < menorNumeroCamisetas:
        menorNumeroCamisetas = numeroCamisetas
        nomeVendedorMenor = nome
    
    print("---------------------------")
    nome = input("=> Informe o nome do vendedor: ")
    nome = nome.capitalize()

print(f"=> Total gasto com pagamento de vendedores: R${totalPagamento}")
print(f"=> Nome do vendedor que vendeu a menor quantidade de camisetas: {nomeVendedorMenor}")