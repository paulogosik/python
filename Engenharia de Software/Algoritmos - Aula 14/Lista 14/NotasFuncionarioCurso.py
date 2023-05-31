listaFuncionarios = []
funcionario = []
i = 0

while i < 3:
    funcionario = []
    funcionario.append(input(f"=> Informe o nome do funcionário {i + 1}: "))
    funcionario.append(input(f"=> Informe o setor do funcionário {i + 1}: "))
    funcionario.append(float(input(f"=> Informe o nota escrita do funcionário {i + 1}: ")))
    funcionario.append(float(input(f"=> Informe o nota prática do funcionário {i + 1}: ")))
    print("----------------------------")
    
    listaFuncionarios.append(funcionario)
    
    i += 1
    
i = 0
while i < len(listaFuncionarios):
    print(f"=> Funcionário: {listaFuncionarios[i][0]} - Setor: {listaFuncionarios[i][1]} - Nota escrita: {listaFuncionarios[i][2]} - Nota prática: {listaFuncionarios[i][3]}")
    
    i += 1
print("----------------------------")

print(f"=> Funcionários aprovados: ")
i = 0
while i < len(listaFuncionarios):
    if (listaFuncionarios[i][2] + listaFuncionarios[i][3]) >= 7:
        print(f"=> {listaFuncionarios[i][0]}")
    
    i += 1