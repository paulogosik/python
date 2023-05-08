i = 0

while i < 10:
    i += 1
    nome = input(f"=> Qual o nome do paciente {i}? ")
    peso = float(input(f"=> Qual o peso do paciente {i}? "))
    altura = float(input(f"=> Qual a altura do paciente {i}? Em metros. "))
    print("")

    imc = peso / (altura**2)
    nome = nome.capitalize()
    print(f"=> Paciente: {nome}")

    if imc < 18.5:
        print("=> Situação: Abaixo do peso")
        print("-----------------------------------")
    elif imc >= 18.5 and imc < 25:
        print("=> Situação: Peso normal")
        print("-----------------------------------")
    elif imc >= 25 and imc < 30:
        print("=> Situação: Acima do peso")
        print("-----------------------------------")
    else:
        print("=> Situação: Obesidade")
        print("-----------------------------------")
