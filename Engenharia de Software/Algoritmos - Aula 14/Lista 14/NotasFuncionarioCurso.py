listaFuncionarios = []
funcionario = []
i = 0

while i < 3:
    funcionario = []
    funcionario.append(input(f"=> Informe o nome do funcionário {i + 1}: "))
    funcionario.append(input(f"=> Informe o setor do funcionário {i + 1}: "))
    funcionario.append(input(f"=> Informe o nota escrita do funcionário {i + 1}: "))
    funcionario.append(input(f"=> Informe o nota prática do funcionário {i + 1}: "))
    print("----------------------------")
    
    listaFuncionarios.append(funcionario)
    
    i += 1
    
i = 0
while i < len(listaFuncionarios):
    print(f"=> Funcionário: {listaFuncionarios[]}")
    
    i += 1