opc = "S"
i = 0
opc = opc.upper()

while opc != "N":
    i += 1
    print(f"=> Partida {i}")
    horaI = int(input("=> Informe o horário inicial da partida: "))
    horaF = int(input("=> Informe o horário final da partida: "))
    
    if horaF < horaI:
        horaF += 24
            
    duracao = horaF - horaI
    
    if duracao > 8:
        print(f"=> Uma partida não pode durar mais de 8 horas.")
    else:
        print(f"=> A partida durou {duracao}h")
        
    print("--------------------------")
    opc = input("=> Deseja continuar? (S/N). ")
    opc = opc.upper()
    print("--------------------------")