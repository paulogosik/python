salarioAlto = 0
contFunc = 0
contSalario = 0
salarioMaior = 0
salarioMenor = 0

nome = input("=> Qual o nome do funcionário? ")

while nome != "fim":
    horas = float(input("=> Informe a quantidade de horas trabalhadas: "))
    valorHora = float(input("=> Informe o valor recebido por hora trabalhada: "))
    
    salario = horas * valorHora
    print(f"=>Nome: {nome}\n"
          f"=> Salário: {salario}")
    
    contFunc += 1
    contSalario += salario
    
    if salario > salarioMaior:
        salarioMaior = salario
    if salarioMenor == 0:
        salarioMenor = salario
    elif salarioMenor > salario:
        salarioMenor = salario
    print('-------------------------------')
    nome = input("=> Qual o nome do funcionário? ")
    
print("--------------------------")
mediaSalario = contSalario / contFunc
print(f"=> Média dos salários: {mediaSalario}")
print(f"=> Maior salário: {salarioMaior}")
print(f"=> Menor salário: {salarioMenor}")